/*
 * package competition;


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class NPuzzle {
    static void nextMove(int k,int [][] grid){
        //Your logic here
    Tuple1 pacman = new Tuple1(pacman_r,pacman_c,0);
    Tuple1 food = new Tuple1(food_r,food_c,0);
    Tuple1 size = new Tuple1(r,c,-1);
    
    Comparator<Tuple1> comp = new tupleComp();
    PriorityQueue<Tuple1> toVisit = new PriorityQueue<Tuple1>(r*c,comp);
    
    int[][] dist = new int[r][c];
    Tuple1[][] prev = new Tuple1[r][c];
    Tuple1 dummy = new Tuple1(-1,-1,1000);
    
    for(int i=0 ; i<r ; i++){
    	for(int j=0 ; j<c ; j++){
    		dist[i][j] = 1000;
    		prev[i][j] = dummy;
    	}
    }
    
    dist[pacman.r][pacman.c] = 0;
    
    toVisit.add(pacman);
    
    while(!toVisit.isEmpty()){
        Tuple1 curNode = toVisit.poll();
                
        if(grid[curNode.r][curNode.c]=='.'){
        	break;
        }
        
        int[] rowChange = {-1,0,0,1};
        int[] colChange = {0,-1,1,0};
        
        for(int i=0 ; i<4 ; i++){
            Tuple1 up = new Tuple1();
            up.r = curNode.r + rowChange[i];
            up.c = curNode.c + colChange[i];
            if(grid[up.r][up.c]=='-'||grid[up.r][up.c]=='.'){
                if(grid[up.r][up.c]=='-'){
            	   grid[up.r][up.c] = 'v';
            	}
            	   
                int temp = dist[curNode.r][curNode.c]+1;
        		   
                if(temp<dist[up.r][up.c]){
        		  dist[up.r][up.c]= temp;
        		  prev[up.r][up.c] = curNode;
        		  up.cost = temp + Math.abs(food.r-up.r) + Math.abs(food.c-up.c);
        		}
                toVisit.add(up);
             }
        }
        
    }
    
    Stack<Tuple1> path = new Stack<Tuple1>();
    path.push(food);
    while(true){
    	try{
    		Tuple1 top = path.peek();
        	Tuple1 parent = prev[top.r][top.c];
        	path.push(parent);
    	}
    	catch(Exception e){
    		Tuple1 dummy1 = path.pop();
    		break;
    	}
    }
    
    String pathStr = "";
    
    while(!path.empty()){
    	Tuple1 temp = path.pop();
    	pathStr = pathStr + temp.r + " " + temp.c + "\n";
    }
    
    //System.out.println(count);
    //System.out.println(trav);
    System.out.println(dist[food.r][food.c]);
    System.out.println(pathStr);
    }
    
    public static void main(String[] args) {
        // Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. 
        Scanner scan = new Scanner(System.in);

        int k = scan.nextInt();
        
        int[][] grid = new int[k][k];
        for(int i=0 ; i<k ; i++){
        	for(int j=0 ; i<k ; i++){
        		grid[i][j] = scan.nextInt();
        	}
        }
        
        nextMove( k, grid);
    }
}

class Node{
	int[][] grid;
	int cost;
	public Node(int[][] grid, int cost){
		
    }
    public Node(){
    	
    }
}

class nodeComp implements Comparator<Node>{

	@Override
	public int compare(Node arg0, Node arg1) {
		// TODO Auto-generated method stub
		if(arg0.cost < arg1.cost){
			return -1;
		}
		else if(arg0.cost > arg1.cost){
			return 1;
		}
		else{
			return 0;
		}
	}	
}
*/