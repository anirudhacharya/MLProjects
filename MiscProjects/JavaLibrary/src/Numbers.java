import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;


public class Numbers {
	
	public List<Integer> getNumberArray(int n){
		
		List<Integer> numbers = new ArrayList<Integer>();
		Random random = new Random();
		
		for(int i=0; i<n; i++){
			int num = random.nextInt(100000);
			numbers.add(num);
		}
		return numbers;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random random = new Random();
		List<Integer> numbers = new ArrayList<Integer>();
		
		File file = new File("number.txt");
		FileWriter fwrite = null;
		try {
			fwrite = new FileWriter(file);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		PrintWriter pwrite = new PrintWriter(fwrite);
		
		for(int i=0; i<100000; i++){
			int num = random.nextInt(1000000);
			pwrite.println(Integer.toString(num));
		}
	}
}
