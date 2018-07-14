package collabFilter;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileFilter;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map.Entry;
import java.util.regex.Pattern;

class ValueComparator implements Comparator<Integer> {

    Map<Integer, Double> base;
    public ValueComparator(Map<Integer, Double> base) {
        this.base = base;
    }

    // Note: this comparator imposes orderings that are inconsistent with equals.    
    public int compare(Integer a, Integer b) {
        if (base.get(a) >= base.get(b)) {
            return -1;
        } else {
            return 1;
        } // returning 0 would merge keys
    }
}
public class BigCreateReco {
	
//	static double[][] user_item = new double[6][5];
	//static int num_users=2649429, num_items=427;
	static int num_users=150, num_items=427;
	
	//initialize feature space dimensionality to your chosen number
	static int factor_dim = 5;
	//initialize the user vector set
//	static double [][] user_vec = new double[num_users][factor_dim];
	//initialize the item vector set
//	static double [][] item_vec = new double[num_items][factor_dim];
	
	static Map<Point, Double> matrix = new HashMap<Point, Double>();
	static Map<Point, Double> user_vec = new HashMap<Point, Double>();
	static Map<Point, Double> item_vec = new HashMap<Point, Double>();
	static Process p;
	static File file;
	static FileWriter writer;
	static Scanner s;
	static String ret;
	static String[] ret_array;
	static Point temp = new Point(-1,-1);
	static int keep_track=0;
	
	public static void genBigData() throws IOException {
	
		
		File folder = new File("dataset/training_set");
		File[] listOfFiles = folder.listFiles();
   //     int largeSoFar=0;
        int currentUserId=0;
        double currentUserRating=0;
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
		        	  currentUserRating=Double.parseDouble(splitLine[1]);
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
		
		    	Double val = matrix.get(new Point(userID, movieID));
		    		System.out.println(val+" ");
		  
		
	}

	
/*	public static void write_to_file(String to_write, File file) throws IOException{
        FileWriter writer = new FileWriter(file.getAbsolutePath()); 
        writer.write(to_write);
        System.out.println("string u are writing "+to_write);
        writer.close();
	}
	*/
	
	public static void factorize(Point to_check, int flag) throws IOException{
		int i=to_check.x;
		int j=to_check.y;
		double rating = matrix.get(to_check);
		String to_write = rating+"\n";
		int k;
		
	//	System.out.println("Now factorizing rating by user: "+i+" for item "+j);
	//	System.in.read();
		if(flag==0){
			for(k=0; k<factor_dim; k++){
				temp.x=i;
				temp.y=k;
				to_write+=user_vec.get(temp);
				if(k<factor_dim-1) to_write+=",";
			}
			to_write+="\n";
			for(k=0; k<factor_dim; k++){
				temp.x=j;
				temp.y=k;
				to_write+=item_vec.get(temp);
				if(k<factor_dim-1) to_write+=",";
			}
		}
		else if(flag==1){
			for(k=0; k<factor_dim; k++){
				temp.x=j;
				temp.y=k;
				to_write+=item_vec.get(temp);
				if(k<factor_dim-1) to_write+=",";
			}
			to_write+="\n";
			for(k=0; k<factor_dim; k++){
				temp.x=i;
				temp.y=k;
				to_write+=user_vec.get(temp);
				if(k<factor_dim-1) to_write+=",";
			}
		}
		
		file = new File("in_file.txt");
      //  System.out.println("Final filepath : " + file.getAbsolutePath());
		//write_to_file(to_write, file);	
        writer = new FileWriter(file.getAbsolutePath()); 
        writer.write(to_write);
      //  System.out.println("string u are writing "+to_write);
        writer.close();
		
		p = Runtime.getRuntime().exec("C:\\Python34\\python quadProg.py");
		file = new File("out.txt");
		s = new Scanner(file);
    	ret = s.nextLine();	
    	s.close();
		ret_array = ret.split(" ");
		for(int m=0; m<ret_array.length; m++){
			if(flag==0) {//update user vector
				temp.x=i;
				temp.y=m;
				user_vec.put(temp, Double.parseDouble(ret_array[m]));
				//user_vec[i][m] = Double.parseDouble(ret_array[m]);//assuming ret_array.length=factor_dim
			}
			else if(flag==1) {
				temp.x=j;
				temp.y=m;
				item_vec.put(temp, Double.parseDouble(ret_array[m]));
				//item_vec[j][m] = Double.parseDouble(ret_array[m]);
			}
		}
	/*	if(keep_track++>=100){
			System.gc();
			keep_track=0;
		}
		*/
	}
	
	public static void main(String[] args) throws IOException{
		createReco cr = new createReco();
		
		genBigData();
		
		Point to_check = new Point(-1,-1);
		
		int[] item_flag = new int[num_items];
		for(int l=0;l<num_items;l++){
			item_flag[l]=0;
		}
		
		
		for(int j=0; j<factor_dim; j++){
			for(int i=0; i<num_users; i++){
				
				user_vec.put(new Point(i,j), 1.0);
				//user_vec[i][j]=0.0;
			
			}
			for(int i=0; i<num_items; i++){
				
				item_vec.put(new Point(i,j), 0.0);
				//item_vec[i][j]=0.0;
			
			}
			
		}
		
		System.out.println("finished user and item vector creation");
		
	//	if(matrix.containsKey(new Point(6,157))) System.out.println("Success 6, 157");
		
		//loop over the sparse matrix
		long QP_start=System.currentTimeMillis();
		keep_track=0;
		for(int i=0;i<num_users;i++){
			for(int j=0; j<num_items; j++){
				to_check.x = i;
				to_check.y = j;
				Double val=matrix.get(to_check);
				//System.out.println("value of rating is "+val);
				if(matrix.containsKey(to_check)){ //non sparse
					keep_track++;
					if(item_flag[j]==0){
						item_flag[j]=1;
						for(int k=0; k<factor_dim; k++)
							item_vec.put(to_check, 1.0);
					}
					
					factorize(to_check,0);
					factorize(to_check,1);
				}
			}
		}
		long QP_end = System.currentTimeMillis();
		long QP_elapsed = QP_end - QP_start;
		System.out.println("Elpased time for QP factorization for "+num_users+" is "+QP_elapsed+" and #non-sparse entries are "+keep_track);
		
		
		System.out.println("Enter user id:");
		 int user_id;
		    try {
		      Scanner sc = new Scanner (System.in);     
		      user_id = sc.nextInt();
		      sc.close();
		    } catch (NumberFormatException ex) {
		      System.err.println("Not a valid number: " + ex);
		      return;
		    }
		   System.out.println("read "+user_id);
		    
		int item=0;
		int counter=0;
		for(item=0;item<num_items;item++){
			to_check.x=user_id;
			to_check.y=item;
			if(matrix.containsKey(to_check)){
				System.out.println("user "+user_id+" rating for item "+item+" before matrix completion is "+matrix.get(to_check));
				if(counter==6) matrix.remove(to_check);
				counter++;
			}
		}
		
		long reco_start_time =System.currentTimeMillis();
		
		Point user_temp = new Point(-1,-1);
		Point item_temp = new Point(-1,-1);
		double fetch_rate=0.0;
		int rate_user=0, rate_item=0; //predict rating of every -1 entry
		for(rate_user=0; rate_user<num_users; rate_user++){
			for(rate_item=0; rate_item<num_items; rate_item++){
				to_check.x=rate_user;
				to_check.y=rate_item;
				if(!matrix.containsKey(to_check)){
					matrix.put(to_check, 0.0);
					for(int i=0;i<factor_dim; i++){
						fetch_rate=matrix.get(to_check); 
						user_temp.x=rate_user;
						user_temp.y=i;
						item_temp.x=rate_item;
						item_temp.y=i;
						matrix.put(to_check, fetch_rate+user_vec.get(user_temp)*item_vec.get(item_temp));
					}
				}
			}
		}
		
		long reco_end_time = System.currentTimeMillis();
		long elapsed_reco=reco_end_time-reco_start_time;
		System.out.println("difference in times for recommendation for "+num_users+" users is "+elapsed_reco);
		
	/*	for(int i=0; i<num_users; i++){
			System.out.println("user "+i+" vector:");
			for(int f=0; f<factor_dim; f++){
				user_temp.x=i;
				user_temp.y=f;
				System.out.print(user_vec.get(user_temp)+" ");
			}
			System.out.println();
		}
		for(int i=0; i<num_items; i++){
			System.out.println("item "+i+" vector:");
			for(int f=0; f<factor_dim; f++){
				item_temp.x=i;
				item_temp.y=f;
				System.out.print(item_vec.get(item_temp)+" ");
			}
			System.out.println();
		}
		for(int i=0;i<num_users;i++){
			for(int j=0;j<num_items;j++){
				to_check.x=i;
				to_check.y=j;
				System.out.println("rating value for user:"+i+" and item "+j+" is "+matrix.get(to_check)+"\ndone");
			}
		}
	*/	
		
		//after matrix completion ratings for selected user
		Map<Integer, Double> map = new HashMap<Integer,Double>();
		keep_track=0;
		
		for(int usr=0; usr<num_users; usr++){
			for(item=0;item<num_items;item++){
				to_check.x=usr;
				to_check.y=item;
				if(matrix.get(to_check)>0){
					keep_track++;
				}				
			}
		}
		System.out.println("Density of the matrix is currently "+keep_track);
		
		for(item=0;item<num_items;item++){
			to_check.x=user_id;
			to_check.y=item;
			if(matrix.get(to_check)>0){
				System.out.println("User "+user_id+" rates item "+item+"with "+matrix.get(to_check));
			}
			//map.put(item, matrix.get(to_check));		
			
		}
		/*ValueComparator bvc =  new ValueComparator(map);
		TreeMap<Integer,Double> sorted_map = new TreeMap<Integer,Double>(bvc);
        sorted_map.putAll(map);
        
        Iterator it = sorted_map.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry)it.next();
            System.out.println("user item pair after matrix completion for selected user "+pair.getKey() + " = " + pair.getValue());
            it.remove(); // avoids a ConcurrentModificationException
        }
        
		*/	
	if(matrix.containsKey(new Point(403531,9))) System.out.println("Success");
	//System.in.read();
		return;	
	}

}
