

import argparse
import ast
import glob
import json
import os
import time
import subprocess as sb
import sys
import zipfile

sb.call([sys.executable, "-m", "pip", "install", 'gluoncv==0.6.0']) 

import gluoncv as gcv
from gluoncv.data.batchify import Tuple, Stack, Pad
from gluoncv.data.transforms.presets.ssd import SSDDefaultTrainTransform, SSDDefaultValTransform
from gluoncv.utils import viz
from gluoncv.utils.metrics.voc_detection import VOC07MApMetric
import mxnet as mx
from mxnet import gluon, nd, autograd
import numpy as np
from mxnet.contrib import amp




class GTDataset(gluon.data.Dataset):
    """
    Custom Dataset to handle SageMaker Ground Truth annotation
    Arbitrary hard-coded train-val split: 85, 15
    """
    def __init__(self, gt_prefix, data_path='data', split='train', manifest_name='output.manifest'):
        """
        Parameters
        ---------
        data_path: str, Path to the data folder, default 'data'
        split: str, Which dataset split to request, default 'train'
    
        """
        self.data_path = data_path
        self.gt_prefix = gt_prefix
        self.image_info = []
        with open(os.path.join(data_path, manifest_name)) as f:
            lines = f.readlines()
            for line in lines:
                info = json.loads(line[:-1])
                if len(info[self.gt_prefix]['annotations']):
                    self.image_info.append(info)
                    
        assert split in ['train', 'val']
        
        l = len(self.image_info)
        if split == 'train':
            self.image_info = self.image_info[:int(0.85*l)]
        if split == 'val':
            self.image_info = self.image_info[int(0.85*l):]

        
        
    def __getitem__(self, idx):
        """
        Parameters
        ---------
        idx: int, index requested

        Returns
        -------
        image: nd.NDArray
            The image 
        label: np.NDArray bounding box labels of the form [[x1,y1, x2, y2, class], ...]
        """
        info = self.image_info[idx]
        image = mx.image.imread(os.path.join(self.data_path, info['source-ref'].split('/')[-1]))
        boxes = info[self.gt_prefix]['annotations']
        label = []
        for box in boxes:
            label.append([box['left'], box['top'], box['left']+box['width'], box['top']+box['height'], 0])
        
        return image, np.array(label)
        
    def __len__(self):
        return len(self.image_info)




def validate(net, val_data, ctx, classes, size):
    """
    Compute the mAP for the network on the validation data
    """
    metric = VOC07MApMetric(iou_thresh=0.5, class_names=classes)
    net.set_nms(0.2)
    for ib, batch in enumerate(val_data):
        
        data = gluon.utils.split_and_load(batch[0], ctx_list=ctx, batch_axis=0, even_split=False)
        label = gluon.utils.split_and_load(batch[1], ctx_list=ctx, batch_axis=0, even_split=False)
        det_bboxes, det_ids, det_scores = [],[],[]
        gt_bboxes,gt_ids = [], []
        
        for x, y in zip(data, label):
            ids, scores, bboxes = net(x)
            det_ids.append(ids)
            det_scores.append(scores)
            det_bboxes.append(bboxes.clip(0, batch[0].shape[2]))
            gt_ids.append(y.slice_axis(axis=-1, begin=4, end=5))
            gt_bboxes.append(y.slice_axis(axis=-1, begin=0, end=4))
            
            # metric.update(det_bboxes, det_ids, det_scores, gt_bboxes, gt_ids, [None])  # For older versions of GluonCV
            metric.update(det_bboxes, det_ids, det_scores, gt_bboxes, gt_ids[0], None)
    return metric.get()


if __name__ == '__main__':


    # Create environment variables if not running on SageMaker
    try:
        len(os.environ['SM_MODEL_DIR'])
    except:
        os.environ['SM_MODEL_DIR'] = 'local'

    try:
        len(os.environ['SM_CHANNEL_DATA'])
    except:
        os.environ['SM_CHANNEL_DATA'] = 'local'

    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--classes', type=str, help='names of the classes in the shape [name1, name2]')
    parser.add_argument('--gt-prefix', type=str, help='prefix of the SageMaker Ground Truth annotation task')
    parser.add_argument('--batch', type=int, default=10, help='batch size per GPU')
    parser.add_argument('--warmup_begin_lr', type=float, default=0.001, help='initial learning rate')
    parser.add_argument('--lr-multiplier', type=int, default=1, help='peak learning rate as a multiple of lr_start')
    parser.add_argument('--epoch-peak', type=float, default=0.3, help='epoch of max learning rate, as a fraction of total epochs')
    parser.add_argument('--max-update', type=float, default=0.9, help='epoch after which learning rate is constant')
    parser.add_argument('--final-lr', type=float, default=0.0001, help='final learning rate')
    parser.add_argument('--wd', type=float, default=0.0004, help='weight decay')
    parser.add_argument('--momentum', type=float, default=0.9)
    parser.add_argument('--image-size', type=int, default=400)
    parser.add_argument('--num-workers', type=int, default=8)
    parser.add_argument('--epochs', type=int, default=16)
    parser.add_argument('--network', type=str, default='ssd_512_resnet50_v1_coco', help='pre-trained gluoncv net')
    parser.add_argument('--pretrained', type=str, default='True', help='fine tune or not')
    parser.add_argument('--data-location', type=str, default=os.environ['SM_CHANNEL_DATA'], help='local path to store raw images and manifest')
    parser.add_argument('--dataset-name', type=str, default='dataset.zip', help='name of the zip containing images and manifest')
    parser.add_argument('--save-dir', type=str, default=os.environ['SM_MODEL_DIR'], help='local path to store model')
    parser.add_argument('--save-to', type=str, default='ssd.params', help='artifact name')
    parser.add_argument('--checkpoint', type=str, default='True', help='checkpoint everytime epoch mAP improves')    

    args, _ = parser.parse_known_args()
    
        
    classes = ast.literal_eval(args.classes)
    batch_size = args.batch
    image_size = args.image_size
    epochs = args.epochs
    ctx = [mx.gpu(0)] if mx.context.num_gpus() > 0 else [mx.cpu()]  # train in one GPU only


    # bring data
    with zipfile.ZipFile(os.path.join(args.data_location, args.dataset_name), "r") as zip_ref:
        zip_ref.extractall(args.data_location)

    train_images = glob.glob(args.data_location + '/*.jpg')
    print('We have {} images'.format(len(train_images)))

    # instantiate datasets
    train_dataset = GTDataset(data_path=args.data_location, gt_prefix=args.gt_prefix, split='train')
    validation_dataset = GTDataset(data_path=args.data_location, gt_prefix=args.gt_prefix, split='val')
    
    print('There are {} training images, {} validation images'
        .format(len(train_dataset), len(validation_dataset)))


    # instantiate the network
    net = gcv.model_zoo.get_model(args.network, pretrained=ast.literal_eval(args.pretrained))
    net.reset_class(classes)


    # train data iterator
    with autograd.train_mode():
        _, _, anchors = net(mx.nd.zeros((1, 3, image_size, image_size)))
    train_transform = SSDDefaultTrainTransform(image_size, image_size, anchors)
    batchify_fn = Tuple(Stack(), Stack(), Stack())  # stack image, cls_targets, box_targets
    train_data = gluon.data.DataLoader(
        train_dataset.transform(train_transform),
        batch_size,
        True,
        batchify_fn=batchify_fn,
        last_batch='rollover',
        num_workers=args.num_workers)

    # validation data iterator
    val_transform = SSDDefaultValTransform(image_size, image_size)
    batchify_fn = Tuple(Stack(), Pad(pad_val=-1))
    val_data = gluon.data.DataLoader(
        validation_dataset.transform(val_transform),
        batch_size,
        False,
        batchify_fn=batchify_fn,
        last_batch='keep',
        num_workers=args.num_workers)


    # learning rate schedule
    lr = mx.lr_scheduler.CosineScheduler(
        max_update=int(args.max_update*args.epochs),
        base_lr=args.lr_multiplier*args.warmup_begin_lr,
        final_lr=args.final_lr,
        warmup_steps=int(args.epoch_peak*args.epochs),
        warmup_begin_lr=args.warmup_begin_lr)


    # instantiate the optimizer
    net.collect_params().reset_ctx(ctx)
    trainer = gluon.Trainer(
        net.collect_params(), 'sgd', {'wd': args.wd, 'momentum': args.momentum})

    
    mbox_loss = gcv.loss.SSDMultiBoxLoss()
    ce_metric = mx.metric.Loss('CrossEntropy')
    smoothl1_metric = mx.metric.Loss('SmoothL1')


    best_val = 0
    tr_start = time.time()

    for epoch in range(args.epochs):
        ep_start = time.time()
        print('learning rate set to ' + str(lr(epoch)))
        trainer.set_learning_rate(lr(epoch))
        net.hybridize(static_alloc=True, static_shape=True)
        ce_metric.reset()
        smoothl1_metric.reset()

        for i, batch in enumerate(train_data):
    
            data = gluon.utils.split_and_load(batch[0], ctx_list=ctx, batch_axis=0)
            cls_targets = gluon.utils.split_and_load(batch[1], ctx_list=ctx, batch_axis=0)
            box_targets = gluon.utils.split_and_load(batch[2], ctx_list=ctx, batch_axis=0)
    
            with autograd.record():
                cls_preds, box_preds = [], []
                for x in data:
                    cls_pred, box_pred, _ = net(x)
                    cls_preds.append(cls_pred)
                    box_preds.append(box_pred)
                sum_loss, cls_loss, box_loss = mbox_loss(cls_preds, box_preds, cls_targets, box_targets)
                autograd.backward(sum_loss)
    
            trainer.step(1)
            ce_metric.update(0, [l * batch_size for l in cls_loss])
            smoothl1_metric.update(0, [l * batch_size for l in box_loss])
            name1, loss1 = ce_metric.get()
            name2, loss2 = smoothl1_metric.get()
                
        name, val = validate(net, val_data, ctx, classes, image_size)

        ep_stop = time.time()
        
        print('[Epoch {}] Training time: {}'.format(epoch, ep_stop - ep_start))  # training time
        print('[Epoch {}] Learning rate: {}'.format(epoch, trainer.learning_rate))  # learning rate
        print('[Epoch {}] Validation mAP: {}'.format(epoch, val[0]))  # mAP

        # If checkpoint is activated and validation accuracy improve, save the parameters
        if ast.literal_eval(args.checkpoint):
            if val[0] > best_val:
                net.save_parameters(os.path.join(args.save_dir, args.save_to))
                best_val = val[0]
            print("Saving the parameters, best mAP {}".format(best_val))

    if not ast.literal_eval(args.checkpoint):
        net.save_parameters(os.path.join(args.save_dir, args.save_to))

    tr_stop = time.time()
    print('training time: {}s'.format(tr_stop - tr_start))
