package designPatterns.producerConsumer;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author aachy
 *
 */
public class Match {
    private final String name;

    private final List<Message> updates;

    public Match(String name, List<String> matchInfo) {
        this.name = name;
        this.updates = new ArrayList<Message>();
        createUpdateList(matchInfo);
    }

    private void createUpdateList(List<String> matchInfo) {
        createMatchList(matchInfo);
        Collections.sort(updates);
    }

    private void createMatchList(List<String> matchInfo) {
        // TODO Auto-generated method stub
        // parse the string input and
    }

    public String getName() {
        return name;
    }

    public List<Message> getUpdates() {
        return updates;
    }
}
