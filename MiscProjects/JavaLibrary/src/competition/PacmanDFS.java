package competition;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PacmanDFS {
static void dfs(int r, int c, int pacman_r, int pacman_c, int food_r, int food_c, char [][] grid){
        //Your logic here
    Tuple pacman = new Tuple(pacman_r,pacman_c);
    Tuple food = new Tuple(food_r,food_c);
    Tuple size = new Tuple(r,c);
    
    Stack<Tuple> toVisit = new Stack<Tuple>();
    
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
    int travCount = 0;
    String trav = "";
    
    toVisit.push(pacman);
    grid[pacman.r][pacman.c] = 'v';
    
    while(!toVisit.empty()){
        Tuple curNode = toVisit.pop();
        travCount++;
        if(grid[curNode.r][curNode.c]=='e'){
        	continue;
        }
        
        if(grid[curNode.r][curNode.c]=='.'){
        	//travCount++;
        	trav = trav + curNode.r + " " + curNode.c;
            break;
        }
        
        grid[curNode.r][curNode.c] = 'e';
        trav = trav + curNode.r + " " + curNode.c + "\n";
        
        int[] rowChange = {-1,0,0,1};
        int[] colChange = {0,-1,1,0};
        
        for (int i=0 ; i<4 ; i++){
            Tuple nbr = new Tuple();
            nbr.r = curNode.r + rowChange[i];
            nbr.c = curNode.c + colChange[i];
            
            if(grid[nbr.r][nbr.c]=='-'||grid[nbr.r][nbr.c]=='.'){
                if(grid[nbr.r][nbr.c]=='-'){
            	   grid[nbr.r][nbr.c] = 'v';
            	}
                
                int temp = dist[curNode.r][curNode.c]+1;
        		   
                if(temp < dist[nbr.r][nbr.c]){
        		  dist[nbr.r][nbr.c]= temp;
        		  prev[nbr.r][nbr.c] = curNode;
        		}
                
                toVisit.push(nbr);
                //travCount++;
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
    
    System.out.println(travCount);
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

        dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid);
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