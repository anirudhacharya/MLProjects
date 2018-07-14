import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PolarAngles {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        Comparator<Point> comp = new ComparePoints();
        
        int N = scan.nextInt();
        PriorityQueue<Point> pq = new PriorityQueue<Point>(N,comp);
        for(int i=0 ; i<N ; i++){
        	
        	int x = scan.nextInt();
        	int y = scan.nextInt();
        	pq.add(new Point(x,y));
        }
        while(!pq.isEmpty()){
        	Point p = pq.poll();
        	System.out.println(p.x+" "+p.y);
        }
    }
}
class Point{
	int x,y;
	public Point(int x, int y){
		this.x = x;
		this.y = y;
	}
}
class ComparePoints implements Comparator<Point>{
	
	public double getAngle(Point pt){
		double angle = Math.atan2(pt.y, pt.x);
		if(angle>=0)
			return angle;
		else
			return angle+(2*Math.PI);
	}
	
	public double distance(Point pt){
		return Math.pow(pt.x, 2)+ Math.pow(pt.y, 2);
	}

	@Override
	public int compare(Point p1, Point p2) {
		// TODO Auto-generated method stub
		if(getAngle(p1)>getAngle(p2)){
			return 1;
		}
		else if(getAngle(p1)<getAngle(p2)){
			return -1;
		}
		else{
			if(distance(p1)>distance(p2)){
				return 1;
			}
			else{
				return -1;
			}
		}
	}
}