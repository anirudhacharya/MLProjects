import java.io.BufferedReader;



import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.net.URL;
import java.net.URLEncoder;

import javax.print.attribute.HashAttributeSet;

import com.google.gson.Gson;
import com.google.gson.JsonIOException;
import com.google.gson.JsonSyntaxException;
import com.google.gson.reflect.TypeToken;



public class ExtractGenre {
    static Map<Integer, String[]> movieMap=new HashMap<Integer, String[]>();
    
    
    
    public static boolean containsIgnoreCase( String haystack, String needle ) {
    	  if(needle.equals(""))
    	    return true;
    	  if(haystack == null || needle == null || haystack .equals(""))
    	    return false; 

    	  Pattern p = Pattern.compile(needle,Pattern.CASE_INSENSITIVE+Pattern.LITERAL);
    	  Matcher m = p.matcher(haystack);
    	  return m.find();
    	}
    
    
    
	
    public static void main(String[] args) throws FileNotFoundException, IOException{
		int counter=1;
		
			File file = new File("movie_titles.txt");
			try(BufferedReader br = new BufferedReader(new FileReader(file))) {
			    for(String line; (line = br.readLine()) != null; counter++ ) {
			   
			        String[] tokens = line.split(",");
			  
			        Integer temp=Integer.parseInt(tokens[0]);
			        String[] strtemp=new String[2];
			        strtemp[0]=tokens[2];
			        movieMap.put(temp, strtemp);
			       
			        
			        if(counter==427) break;
			    }
	
			}
			
		
		
			
			
			try {	
			for(int i=1;i<=427;i++)
			{
			
			String strtemp[]=movieMap.get(i);
			
			
			String movieName=strtemp[0];
			System.out.print("Movie ID : "+i+"\t");
			System.out.print("Movie Name : "+movieName+"\t");
	        String selectedItem = movieName.toString().replace("\\s+", "+");

	        InputStream input = new URL("http://www.omdbapi.com/?t=" + URLEncoder.encode(selectedItem, "UTF-8")).openStream();
	        Map<String, String> map = new Gson().fromJson(new InputStreamReader(input, "UTF-8"), new TypeToken<Map<String, String>>(){}.getType());

	        String title = map.get("Title");
	        String year = map.get("Year");
	        String released = map.get("Released");
	        String runtime = map.get("Runtime");
	        String genre = map.get("Genre");
	        String actors = map.get("Actors");
	        String plot = map.get("Plot");
	        String imdbRating = map.get("imdbRating");
	        String poster = map.get("Poster");

	      
	      if(genre == null)
	    	  strtemp[1]="nothing";
	      else
	    	  strtemp[1]=genre;
	      
	      System.out.print("Movie genre : "+strtemp[1]);
	      System.out.println();
	      
	      movieMap.put(i, strtemp);
	      
			}
	    } catch (JsonIOException | JsonSyntaxException | IOException e){
	        System.out.println(e);
	    }
			
			
			ArrayList<Integer> a=new ArrayList<Integer>();
			a.add(83);
			a.add(167);
			a.add(175);
			a.add(270);
			a.add(275);
			a.add(353);
			a.add(413);
			
			
			
			ArrayList<Integer> b=new ArrayList<Integer>();
			b.add(8);
			b.add(28);
			b.add(52);
			b.add(55);
			b.add(58);
			hitMissRatio(a, b);
	
		}
    
    
    
    
    public static void hitMissRatio(ArrayList<Integer>alreadyRatedMovieID, ArrayList<Integer>newlyRatedMovieID)
    {  
    	double hit=0.00;
    	
    	String alreadyRatedGenres="";
    	for(int i=1;i<=alreadyRatedMovieID.size();i++)
    	{
    		String[] temp=movieMap.get(alreadyRatedMovieID.get(i-1));
    		alreadyRatedGenres+=temp[1]+",";
    	}
    	
    	System.out.println("Cumulative movie genres already rated :"+alreadyRatedGenres);
    	
    	for(int i=1;i<=newlyRatedMovieID.size();i++)
    	{
    		String newlyRatedGenre="";
    		
    		String[] temp=movieMap.get(newlyRatedMovieID.get(i-1));
    		
    		if(temp[1].equals(null))
    			newlyRatedGenre="nothing";
    		else
    			newlyRatedGenre=temp[1];
    		System.out.println("For newly rated movie "+newlyRatedMovieID.get(i-1)+" checking if its current genre "+newlyRatedGenre+" is a subset of oldly rated genre "+alreadyRatedGenres);
    	//	System.out.println("Newly rate movie genre for movie id:"+ newlyRatedMovieID.get(i-1)+" is :"+newlyRatedGenre);
    		if(newlyRatedGenre.equals("nothing"))
    			hit++;
    		else
    		{
    			
    			System.out.println("I came here !");
    		String[] newRateArray=newlyRatedGenre.split(",");
    		for(int k=0;k<newRateArray.length;k++)
    		{
    		if(containsIgnoreCase( alreadyRatedGenres, newRateArray[k]) ) {
      	      System.out.println( "Matching genre "+newRateArray[k]+ " found for newly rated movie id :"+newlyRatedMovieID.get(i-1) );
      	      hit++;
      	      break;
    	    	}	
    		}
    	
    	}
    	}
    	System.out.println("HIT count: "+hit);
    	System.out.println("Total Size "+newlyRatedMovieID.size());
    	double hitRatio=hit/newlyRatedMovieID.size();
    	System.out.println("HIT ratio: "+hitRatio);
    	System.out.println("HIT percentage: "+hitRatio*100 +"%");
     }
    
	
}
