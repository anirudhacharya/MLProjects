
public class AVL extends BST{
	public AVL(){
		super();
	}
	
	@Override
	public Node insert(Node node, int value){
		if(node==null){
			return new Node(value);
		}
		
		else{
			if(value < node.data){
				node.left = this.insert(node.left, value);
			}
			else{
				node.right = this.insert(node.right, value);
			}
			node.height = max(getHeight(node.left), getHeight(node.right))+1;
			int balFactor = getBalFactor(node);
			
			if(balFactor<-1){
				//Right heavy
				if(getBalFactor(node.right)>0){
					//right subtree is left heavy
					//right rotate node.right
					//left rotate node
					node.right = rightRotate(node.right);
					node = leftRotate(node);
				}
				else{
					//right subtree is right heavy
					//left rotate node
					node = leftRotate(node);
				}
			}
			else if(balFactor>1){
				//left heavy
				if(getBalFactor(node.left)<0){
					//left subtree is right heavy
					//left rotate left subtree
					//right rotate node
					node.left = leftRotate(node.left);
					node = rightRotate(node);
				}
				else{
					//left subtree is left heavy
					//right rotate node
					node = rightRotate(node);
				}
			}
		
			return node;
		}
	}
	
	public Node leftRotate(Node node){
		Node right = node.right;
		
		node.right = right.left;
		//if(right.left != null)
			//(right.left).parent = node;
		
		right.left = node;
		//right.parent = node.parent;
		//node.parent = right;
		
		node.height = this.getHeight(node);
		right.height = this.getHeight(right);
		
		return right;
	}
	
	public Node rightRotate(Node node){
		Node left = node.left;
		
		node.left = left.right;
		//if(left.right != null)
			//(left.right).parent = node;
		
		left.right = node;
		//left.parent = node.parent;
		//node.parent = left;
		
		node.height = this.getHeight(node);
		left.height = this.getHeight(left);
		
		return left;
	}
	
	public int getBalFactor(Node node){
		if(node.right == null){
			return (node.left).height;
		}
		else if(node.left == null){
			return -(node.right).height;
		}
		else if(node.right!=null && node.left!=null){
			return ((node.left).height - (node.right).height);
		}
		else{
			return 0;
		}
	}
}
