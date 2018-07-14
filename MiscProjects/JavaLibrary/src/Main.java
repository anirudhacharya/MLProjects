import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.NotSerializableException;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		
		BST bst = new BST();
		//Node node;
		int[] num = {15, 8, 5, 3, 4, 10, 9, 13, 11, 25, 20, 35}; 
			//{15, 8, 25, 5, 10, 20, 35, 3, 9, 13, 4, 11}; 
			//{4,9,5,7,6,11,14,8,9,4};
		//long start0 = System.currentTimeMillis();
		
		//ArrayList<Integer> nums = (ArrayList<Integer>) (new Numbers()).getNumberArray(100);
		//ArrayList<Integer> nums = new ArrayList<Integer>(Arrays.asList(num));
		//long start = System.currentTimeMillis();
		
		//System.out.println("Getting the numbers ... "+(start-start0));
		
		for(int i=0 ; i<num.length ; i++){
			bst.root = bst.insert(bst.root, num[i]);
		}
		
		//long end = System.currentTimeMillis();
		
		//System.out.println("Duration ... "+(end-start));
		/*
		FileOutputStream fileOut = null;
		ObjectOutputStream outStream = null;
		
		try {
			fileOut = new FileOutputStream("bst.ser");
			outStream = new ObjectOutputStream(fileOut);
			outStream.writeObject(bst);
			System.out.println("Tree has been written");
			
		}
		catch (NotSerializableException exception)
        {
			exception.printStackTrace();
			System.out.print("The object is not serializable\n");
         //System.out.print(exception+"\n");
        }
		catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		
		finally{
			try {
				outStream.close();
				fileOut.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} */
		bst.inorder(bst.root);
		System.out.println();
		bst.preorder(bst.root);
		System.out.println();
		bst.postorder(bst.root);
	}

}