import java.util.ArrayList;
import java.util.List;

/**
 * @author aachy
 *
 */
public class HashTable<K, V> {
    public static final int SIZE = 10;
    public int LOAD_FACTOR = 0;
    List<HashNode<K, V>> objects = new ArrayList<HashNode<K, V>>(SIZE);

    public HashNode<K, V> get(int key) {
        int index = hashFunc1(key);
        return objects.get(index);
    }

    public void put(int key, HashNode<K, V> value) {
        int index = hashFunc1(key);
        objects.add(index, value);
    }

    public void delete(int key) {
        int index = hashFunc1(key);
        objects.add(index, null);
    }

    public int hashFunc1(int key) {
        int hash = key % SIZE;
        return hash;
    }
}

class HashNode<K, V> {
    K key;
    V value;

    public HashNode(K key, V value) {
        this.key = key;
        this.value = value;
    }
}
