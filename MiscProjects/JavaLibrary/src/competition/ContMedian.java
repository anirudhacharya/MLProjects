package competition;
/*import java.util.PriorityQueue;


public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
		int[] nums = {34,45,12,78,12,14,9,-23,98,123,345,16};
		for(int i=0 ; i<nums.length ; i++){
			pq.add(nums[i]);
		}
		
		System.out.println(pq.remove(123));
	}

}*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ContMedian{
    /* Head ends here*/
    static void median(String a[],int x[]) {
        Comparator<Integer> cmp = new maxComparator();
        PriorityQueue<Integer> lowHeap = new PriorityQueue<Integer>(10,cmp);
        PriorityQueue<Integer> highHeap = new PriorityQueue<Integer>();
        
        for(int i=0 ; i<a.length ; i++){
            
            if(a[i].equals("a")){
            	if(lowHeap.peek()!=null){
            		if(x[i]>lowHeap.peek()){
                        highHeap.add(x[i]);
                    }
                    else{
                        lowHeap.add(x[i]);
                    }
            	}
            	else{
            		lowHeap.add(x[i]);
            	}
            }
            else if(a[i].equals("r")){
            	if(lowHeap.peek()!=null){
            		if(x[i]>lowHeap.peek()){
                        if(!highHeap.remove(x[i])){
                        	System.out.println("Wrong!");
                        	continue;
                        }
                    }
            		else{
                        if(!lowHeap.remove(x[i])){
                        	System.out.println("Wrong!");
                        	continue;
                        }
                    }
            	}
            	else{
            		if(highHeap.peek()!=null){
            			if(!highHeap.remove(x[i])){
            				System.out.println("Wrong!");
            				continue;
            			}
            		}
                    
                }
            }
                        
            int lowSize = lowHeap.size();
            int highSize = highHeap.size();
            if(lowSize==(highSize+2)){
                highHeap.add(lowHeap.poll());
                lowSize--;
                highSize++;
            }
            if(lowSize==(highSize-2)){
                lowHeap.add(highHeap.poll());
                lowSize++;
                highSize--;
            }
            
            if(lowSize==0 && highSize==0){
                System.out.println("Wrong!");
            }
            else{
                if(lowSize>highSize){
                    System.out.println(lowHeap.peek());
                }
                else if(lowSize<highSize){
                    System.out.println(highHeap.peek());
                }
                else if(lowSize==highSize){
                	double result = (lowHeap.peek()/2.0)+(highHeap.peek()/2.0);
                    if(result%1 == 0){
                        System.out.println((int)(result));
                    }
                    else{
                        DecimalFormat df = new DecimalFormat("#.#");
                        df.setMaximumFractionDigits(100000);
                        System.out.println(df.format(result));
                    }
                    
                }
      
            }
            
        }
    }
    
    /* Tail starts here*/
    
   public static void main( String args[] ){
      
	  long start = System.currentTimeMillis();
      Scanner in = new Scanner(System.in);
      
      int N;
      N = in.nextInt();
   
      String s[] = new String[N];
      int x[] = new int[N];
      
      for(int i=0; i<N; i++){
         s[i] = in.next();
         x[i] = in.nextInt();
      }
   
      median(s,x);
      long stop = System.currentTimeMillis();
      System.out.println(stop-start);
    }
}

class maxComparator implements Comparator<Integer>{
    @Override
    public int compare(Integer x, Integer y){
        if(x>y)
        	return -1;
        else if(x<y)
        	return 1;
        else
        	return 0;
    }
}
