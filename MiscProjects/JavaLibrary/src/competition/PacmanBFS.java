package competition;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PacmanBFS {
static void nextMove(int r, int c, int pacman_r, int pacman_c, int food_r, int food_c, char [][] grid){
        
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
        
        
        // UP
        Tuple up = new Tuple();
        up.r = curNode.r - 1;
        up.c = curNode.c;
        if(up.r>=0){
            if(grid[up.r][up.c]=='-'||grid[up.r][up.c]=='.'){
            	if(grid[up.r][up.c]=='-'){
            		grid[up.r][up.c] = 'v';
            	}
            	int temp = dist[curNode.r][curNode.c]+1;
        		if(temp<dist[up.r][up.c]){
        			dist[up.r][up.c]= temp;
        			prev[up.r][up.c] = curNode;
        		}
                toVisit.add(up);
            }
        }
        
        //LEFT
        Tuple left = new Tuple();
        left.r = curNode.r;
        left.c = curNode.c-1;
        
        if(up.c>=0){
            if(grid[left.r][left.c]=='-'||grid[left.r][left.c]=='.'){
            	if(grid[left.r][left.c]=='-'){
            		grid[left.r][left.c] = 'v';
            		
            	}
            	int temp = dist[curNode.r][curNode.c]+1;
        		if(temp<dist[left.r][left.c]){
        			dist[left.r][left.c]= temp;
        			prev[left.r][left.c] = curNode;
        		}
                toVisit.add(left);
            }
        }
        
        //RIGHT
        Tuple right = new Tuple();
        right.r = curNode.r;
        right.c = curNode.c+1;
        if(right.c < c){
            if(grid[right.r][right.c]=='-'||grid[right.r][right.c]=='.'){
            	if(grid[right.r][right.c]=='-'){
            		grid[right.r][right.c] = 'v';
            		
            	}
            	int temp = dist[curNode.r][curNode.c]+1;
        		if(temp<dist[right.r][right.c]){
        			dist[right.r][right.c]= temp;
        			prev[right.r][right.c] = curNode;
        		}
                toVisit.add(right);
            }
        }
        
        //DOWN
        Tuple down = new Tuple();
        down.r = curNode.r+1;
        down.c = curNode.c;
        if(down.r<r){
            if(grid[down.r][down.c]=='-'||grid[down.r][down.c]=='.'){
            	if(grid[down.r][down.c]=='-'){
            		grid[down.r][down.c] = 'v';
            		
            	}
            	int temp = dist[curNode.r][curNode.c]+1;
        		if(temp<dist[down.r][down.c]){
        			dist[down.r][down.c]= temp;
        			prev[down.r][down.c] = curNode;
        		}
                toVisit.add(down);
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
class Tuple1{ 
	  public int r; 
	  public int c; 
	  public Tuple1(int r, int c) { 
	    this.r = r; 
	    this.c = c; 
	  } 
	  public Tuple1(){  
	  }
} 
}
