package graph;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Djikstra {
static void nextMove(int r, int c, int pacman_r, int pacman_c, int food_r, int food_c, char [][] grid){
        //Your logic here
    Tuple pacman = new Tuple(pacman_r,pacman_c);
    Tuple food = new Tuple(food_r,food_c);
    Tuple size = new Tuple(r,c);
    
    Queue<Tuple> toVisit = new ArrayDeque<Tuple>();
    
    int[][] dist = new int[r][c];
    Tuple[][] prev = new Tuple[r][c];
    Tuple dummy = new Tuple(-1,-1);
    
    for(int i=0 ; i<r ; i++){
    	for(int j=0 ; j<c ; j++){
    		dist[i][j] = 1000;
    		prev[i][j] = dummy;
    	}
    }
    
    dist[pacman.r][pacman.c] = 0;
    
    toVisit.add(pacman);
    
    int count = 0;
   
    String trav = "";
    
    while(!toVisit.isEmpty()){
        Tuple curNode = toVisit.poll();
        count++;        
        if(grid[curNode.r][curNode.c]=='.'){
        	trav = trav + curNode.r + " " + curNode.c;
            break;
        }
        trav = trav + curNode.r + " " + curNode.c + "\n";
        
        int[] nRows = {-1,0,0,1};
        int[] nCols = {0,-1,1,0};
        
        for(int i=0 ; i<nRows.length ; i++){
        	Tuple temp = new Tuple();
            temp.r = curNode.r + nRows[i];
            temp.c = curNode.c + nCols[i];
            if(temp.r>=0){
                if(grid[temp.r][temp.c]=='-'||grid[temp.r][temp.c]=='.'){
                	if(grid[temp.r][temp.c]=='-'){
                		grid[temp.r][temp.c] = 'v';
                	}
                	int temp1 = dist[curNode.r][curNode.c]+1;
            		if(temp1<dist[temp.r][temp.c]){
            			dist[temp.r][temp.c]= temp1;
            			prev[temp.r][temp.c] = curNode;
            		}
                    toVisit.add(temp);
                }
            }
        }
    }
    
    Stack<Tuple> path = new Stack<Tuple>();
    path.push(food);
    while(true){
    	try{
    		Tuple top = path.peek();
        	Tuple parent = prev[top.r][top.c];
        	path.push(parent);
    	}
    	catch(Exception e){
    		Tuple dummy1 = path.pop();
    		break;
    	}
    }
    
    String pathStr = "";
    
    while(!path.empty()){
    	Tuple temp = path.pop();
    	pathStr = pathStr + temp.r + " " + temp.c + "\n";
    }
    
    System.out.println(count);
    System.out.println(trav);
    System.out.println(dist[food.r][food.c]);
    System.out.println(pathStr);
    }
    
public static void main(String[] args) {
        Scanner in = new Scanner(System.in);


        int pacman_r = in.nextInt();
        int pacman_c = in.nextInt();

        int food_r = in.nextInt();
        int food_c = in.nextInt();

        int r = in.nextInt();
        int c = in.nextInt();
    
        char[][] grid = new char[r][c];

        for(int i = 0; i < r; i++) {
            grid[i] = in.next().toCharArray();
      
        }

        nextMove( r, c, pacman_r, pacman_c, food_r, food_c, grid);
    }
}
class Tuple{ 
	  public int r; 
	  public int c; 
	  public Tuple(int r, int c) { 
	    this.r = r; 
	    this.c = c; 
	  } 
    public Tuple(){
        
    }
} 