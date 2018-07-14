import java.awt.Point;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class CreatingUserRating {

	//  private static final int USER_COUNT = 2649429; 
    //	private static final int MOVIE_COUNT = 427;
	static Map<Point, Integer> matrix = new HashMap<Point, Integer>();
	public static void main(String[] args) throws IOException {
	
		
		File folder = new File("dataset/training_set");
		File[] listOfFiles = folder.listFiles();
   //     int largeSoFar=0;
        int currentUserId=0;
        int currentUserRating=0;
        int movieCounter=0;
		for (File file : listOfFiles) {
	
		    if (file.isFile()) {
		    	
		    	String content="";
		    
		     
		        Scanner filescanner = null;
				try {
					filescanner = new Scanner(file);
				} catch (FileNotFoundException e) {
					
					e.printStackTrace();
				}

		        while (filescanner.hasNext())
		        {

		          content = filescanner.nextLine();
		          if(content.contains(":"))
		          {
		        	  content = content.replace(":","");
		        	  movieCounter=Integer.parseInt(content);
		        	  
		          }
		          else
		          {
		        	  
		        	  String[] splitLine = content.split(",");
		        	  currentUserId=Integer.parseInt(splitLine[0]);
		        	  currentUserRating=Integer.parseInt(splitLine[1]);
		        //	  if(currentUserId>=largeSoFar)
		       // 		  largeSoFar=currentUserId;
		        	  System.out.println("USER ID "+splitLine[0]+" AND HIS RATING FOR MOVIE "+movieCounter+" IS "+splitLine[1]);
		        	  matrix.put(new Point(currentUserId,movieCounter ), currentUserRating);
		          }
		        }
		    }
		}
		
	//	System.out.println("TOTAL NUMBER OF USERS: "+largeSoFar);
		printUserRatingMatrix(1945809, 427);
	}

	
	
	private static void printUserRatingMatrix(int userID, int movieID) {
		
		    	Integer val = matrix.get(new Point(userID, movieID));
		    		System.out.println(val+" ");
		  
		
	}

}
