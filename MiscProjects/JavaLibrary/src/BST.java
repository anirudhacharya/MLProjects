import java.io.Serializable;
import java.util.LinkedList;
import java.util.Queue;

public class BST implements Serializable {
    Node root;

    public BST() {
        root = null;
    }

    public Node insert(Node node, int value) {
        if (node == null) {
            return new Node(value);
        }

        else {
            if (value < node.data) {
                node.left = this.insert(node.left, value);
            } else {
                node.right = this.insert(node.right, value);
            }
        }
        return node;
    }

    public Node findMin(Node node) {
        if (node.left == null) {
            return node;
        } else {
            findMin(node.left);
        }
        return node;
    }

    public Node findMax(Node node) {
        if (node.right == null) {
            return node;
        } else {
            findMax(node.right);
        }
        return node;
    }

    public void remove(Node node) {
        Node current = this.root;
        if (node == null) {
            return;
        }
        if (node.data == current.data) {

        } else if (node.data < current.data)
            this.remove(current.left);
        else
            this.remove(current.right);
    }

    public int getHeight(Node node) {
        if (node == null) {
            return 0;
        } else {
            return max(getHeight(node.left), getHeight(node.right)) + 1;
        }
    }

    public Node getNode(Node node, int value) {
        if (node == null) {
            return node;
        }

        if (value == node.data) {
            return node;
        } else if (value < node.data) {
            return getNode(node.left, value);
        } else {
            return getNode(node.right, value);
        }
    }

    public void inorder(Node node) {
        if (node != null) {
            this.inorder(node.left);
            System.out.print(node.data + " ");
            this.inorder(node.right);
        }
    }

    public void postorder(Node node) {
        if (node != null) {
            postorder(node.left);
            postorder(node.right);
            System.out.print(node.data + " ");
        }
    }

    public void preorder(Node node) {
        if (node != null) {
            System.out.print(node.data + " ");
            preorder(node.left);
            preorder(node.right);
        }
    }

    @SuppressWarnings("null")
    public void levelOrder(Node node) {
        Queue<Node> allNodes = new LinkedList<Node>();
        Node current = null;
        allNodes.add(node);

        while (!allNodes.isEmpty()) {
            current = (Node) allNodes.poll();
            System.out.println(current.data + "\t" + current.height);
            if (current.left != null)
                allNodes.add(current.left);
            if (current.right != null)
                allNodes.add(current.right);
        }
    }

    public int max(int a, int b) {
        return a > b ? a : b;
    }

}

class Node implements Serializable {
    int data, height, counter;
    Node left;
    Node right;
    Node parent;

    public Node(int value) {
        data = value;
        left = null;
        right = null;
        height = 1;
        parent = null;
    }

    public boolean hasChildren() {
        if (this.left == null && this.right == null) {
            return false;
        } else {
            return true;
        }
    }

    public int getInfo() {
        return this.data;
    }
}