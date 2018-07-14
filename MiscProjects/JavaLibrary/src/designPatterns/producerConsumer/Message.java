package designPatterns.producerConsumer;

/**
 * @author aachy
 *
 */
public class Message implements Comparable<Message> {

    private final String name;
    private final long time;
    private final String matchTime;
    private final String messageText;

    public Message(String name, long time, String messageText, String matchTime) {
        this.name = name;
        this.matchTime = matchTime;
        this.time = time;
        this.messageText = messageText;
    }

    @Override
    public int compareTo(Message compareMsg) {
        return (int) (time - compareMsg.time);
    }

    @Override
    public String toString() {
        return matchTime + " - " + name + " - " + messageText;
    }

    public String getName() {
        return name;
    }

    public long getTime() {
        return time;
    }

    public String getMatchTime() {
        return matchTime;
    }

    public String getMessageText() {
        return messageText;
    }
}
