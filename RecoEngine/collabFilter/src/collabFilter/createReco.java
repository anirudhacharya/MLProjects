package collabFilter;

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

public class createReco {
	
	static double[][] user_item = new double[4][4];
	static int num_users=4, num_items=4;
	
	//initialize feature space dimensionality to your chosen number
	static int factor_dim = 3;
	//initialize the user vector set
	static double [][] user_vec = new double[num_users][factor_dim];
	//initialize the item vector set
	static double [][] item_vec = new double[num_items][factor_dim];
	
	public static void write_to_file(String to_write, File file) throws IOException{
        FileWriter writer = new FileWriter(file.getAbsolutePath()); 
        writer.write(to_write);
        System.out.println("string u are writing "+to_write);
        writer.close();
	}
	
	public static void factorize(int i, int j, int flag) throws IOException{
		double rating = user_item[i][j];
		String to_write = rating+"\n";
		int k;
		
		if(flag==0){
			for(k=0; k<factor_dim; k++){
				to_write+=user_vec[i][k];
				if(k<factor_dim-1) to_write+=",";
			}
			to_write+="\n";
			for(k=0; k<factor_dim; k++){
				to_write+=item_vec[j][k];
				if(k<factor_dim-1) to_write+=",";
			}
		}
		else if(flag==1){
			for(k=0; k<factor_dim; k++){
				to_write+=item_vec[j][k];
				if(k<factor_dim-1) to_write+=",";
			}
			to_write+="\n";
			for(k=0; k<factor_dim; k++){
				to_write+=user_vec[i][k];
				if(k<factor_dim-1) to_write+=",";
			}
		}
		
		File file = new File("in_file.txt");
        System.out.println("Final filepath : " + file.getAbsolutePath());
		write_to_file(to_write, file);		
		
		Process p = Runtime.getRuntime().exec("C:\\Python34\\python C:\\Users\\vamsi\\workspace\\collabFilter\\quadProg.py");
		BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
		System.out.println(in.readLine()+" done with py run");
		file = new File("out.txt");
		Scanner s = new Scanner(file);
    	String ret = s.nextLine();	
    	s.close();
		String[] ret_array = ret.split(" ");
		System.out.println("array length returned: "+ret_array.length+" ret: "+ret);
		for(int m=0; m<ret_array.length; m++){
			if(flag==0) //update user vector
				user_vec[i][m] = Double.parseDouble(ret_array[m]);//assuming ret_array.length=factor_dim
			else if(flag==1)
				item_vec[j][m] = Double.parseDouble(ret_array[m]);
		}
	}
	
	public static void main(String[] args) throws IOException{
		createReco cr = new createReco();
		
		for(int i=0;i<num_users;i++){
			for(int j=0; j<num_items; j++){
				user_item[i][j]=-1;
			}
		}
	/*	user_item[0][0] = 4.0;
		user_item[0][2]=2.0;
		user_item[0][4]=1.0;
		user_item[1][2]=5.0;
		user_item[1][1]=1.0;
		user_item[2][1]=1.0;
		user_item[2][2]=3.0;
		user_item[2][4]=3.0;
		user_item[3][3]=4.0;
		user_item[3][5]=4.0;
		user_item[4][0]=2.5;
		user_item[4][2]=0.5;
		user_item[4][4]=0.5;
		user_item[5][0]=4.0;
		user_item[5][3]=1.0;
		user_item[5][4]=5.0;
	*/
		user_item[0][0]=4.0;
		user_item[0][2]=1.0;
		user_item[0][3]=2.0;
		user_item[1][0]=5.0;
		user_item[1][1]=4.0;
		user_item[1][3]=2.0;
		user_item[2][0]=1.0;
		user_item[2][1]=2.0;
		user_item[2][3]=5.0;
		user_item[3][1]=1.0;
		user_item[3][2]=5.0;
		user_item[3][3]=4.0;
		
		
		
		for(int j=0; j<factor_dim; j++){
			for(int i=0; i<num_users; i++){
				
				user_vec[i][j]=1;
			
			}
			for(int i=0; i<num_items; i++){
				
				item_vec[i][j]=1;
			
			}
			
		}
		
		//loop over the sparse matrix
		
		for(int i=0;i<num_users;i++){
			for(int j=0; j<num_items; j++){
				if(user_item[i][j]>-1){ //non sparse
					factorize(i,j,0);
					factorize(i,j,1);
				}
			}
		}
		
		
		
		int rate_user=0, rate_item=0; //predict rating of every -1 entry
		for(rate_user=0; rate_user<num_users; rate_user++){
			for(rate_item=0; rate_item<num_items; rate_item++){
				if(user_item[rate_user][rate_item]==-1){
					user_item[rate_user][rate_item]=0.0;
					for(int i=0;i<factor_dim; i++){
						user_item[rate_user][rate_item]+=user_vec[rate_user][i]*item_vec[rate_item][i];
					}
				}
			}
		}
		
		for(int i=0; i<num_users; i++){
			System.out.println("user "+i+" vector:");
			for(int f=0; f<factor_dim; f++){
				System.out.print(user_vec[i][f]+" ");
			}
			System.out.println();
		}
		for(int i=0; i<num_items; i++){
			System.out.println("item "+i+" vector:");
			for(int f=0; f<factor_dim; f++){
				System.out.print(item_vec[i][f]+" ");
			}
			System.out.println();
		}
		for(int i=0;i<num_users;i++){
			for(int j=0;j<num_items;j++){
				System.out.println("rating value for user:"+i+" and item "+j+" is "+user_item[i][j]+"\ndone");
			}
		}
			
	}

}
