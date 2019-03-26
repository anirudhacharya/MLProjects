### Mixed Precision Training

 - to reduce training time and memory by casting compute intensive operations from fp32 to fp16.
 - due to differences in representable ranges, simply converting fp32 to fp16 would result in 
    - gradient underflow - solution : perform loss scaling
    - reductions overflow - solution : accumulate to fp32
    - imprecise weight updates - solution : maintain master weights in fp32
    
we get around these problems with the following techniques.

```
   get weights from fp32 master copy                                         Store weights back into the master copy
                                |                                                      ^   
                                |                                             cast weight gradeints to fp32
                                V                                                      ^ 
                            cast to fp16                                        backward pass --> 
                                |                                                      ^                                   
                                V                                                      |
Input --> cast to fp16 --> forward pass --> cast to fp32 --> Loss calculation --> cast to fp16
```

 - first, cast inputs from fp32 to fp16 for compute intensive operations
 - because using fp16 may cause gradients underflow or overflow, we do the loss calculations in fp32
 - In backward pass, we cast grads back into fp16 so that now the weights and gradients will be in fp16. This will ensure optimal usage of xpu processing power.
   In backward pass grads are smaller than paramters, so in such updates we might lose the parameter updates. We avoid this by maintaining a master copy of weights in fp32.
 - Loss Scaling - to avoid gradient underflow, before computing gradient of fp32 loss, we scale the loss by multiplying with a loss scale factor. By this gradients are pushed to larger values and can safely be represented in fp16. Later while updating the weights we can rescale the weights by dividing them with the same loss scaling factor.


Code and pull request for Nesterov Accelerated Gradient optimizer - https://github.com/apache/incubator-mxnet/pull/14568

