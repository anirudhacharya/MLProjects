package designPatterns.producerConsumer;

import java.util.List;
import java.util.Queue;

/**
 * @author aachy
 *
 */
public class MatchReporter implements Runnable {

    private final Match match;
    private final Queue<Message> queue;

    public MatchReporter(Match curMatch, Queue<Message> queue) {
        this.match = curMatch;
        this.queue = queue;
    }

    @Override
    public void run() {
        long now = System.currentTimeMillis();

        List<Message> matchUpdates = match.getUpdates();

        for (Message message : matchUpdates) {
            delayUntilNextUpdate(now, message.getTime());
            queue.add(message);
        }
    }

    private void delayUntilNextUpdate(long now, long time) {
        while (System.currentTimeMillis() < now + time) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void start() {
        String name = match.getName();
        Thread thread = new Thread(this, name);
        thread.start();
    }
}
