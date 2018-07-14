
public class LinkedList {
	
	Node head = null;
	
	public class Node{
		int value;
		Node next, prev;
		public Node(int value){
			value = value;
			next = null;
			prev = null;
		}
	}
	
	public boolean hasElem(){
		if (head==null)
			return false;
		else
			return true;
	}
	
	public void addNode(int val){
		Node node = new Node(val);
		node.next = this.head;
		if(head!=null){
			head.prev = node;
		}
		this.head = node;
	}
	
	/*public void removeNode(int val){
		Node current = this.head;
		while(current!=null){
			if(current.value==val){
				
			}
			else{
				current = current.next;
			}
		}
	}*/
}
