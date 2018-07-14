package designPatterns.producerConsumer;

import java.util.concurrent.BlockingQueue;

/**
 * @author aachy
 *
 */
public class Teletype implements Runnable {

    private final BlockingQueue<Message> queue;
    private final PrintHead printHead;

    public Teletype(PrintHead printHead, BlockingQueue<Message> queue) {
        this.queue = queue;
        this.printHead = printHead;
    }
    @Override
    public void run() {
        while (true) {
            try {
                Message message = queue.take();
                printHead.print(message.toString());
            } catch (InterruptedException e) {
                printHead.print("error");
            }
        }
    }

    public void destroy() {

    }

    public PrintHead getPrintHead() {
        return printHead;
    }
    public BlockingQueue<Message> getQueue() {
        return queue;
    }
}
