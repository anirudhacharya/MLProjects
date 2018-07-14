package competition;
/*
 * An array of size n is given. The array contains digits from 0 to 9. 
 * I had to generate the maximum number using the digits in the array such that it is divisible by 2, 3 and 5
 * eg: 1 array = 18760, output must be: 8160
 * eg: 2 array = 7776, output must be: “no number can be formed”
 */

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

public class ArrayDivisibility {

	public static void main(String[] args) {
		ArrayList<Integer> nums = new ArrayList<Integer>();
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		ArrayList<Integer> mod1 = new ArrayList<Integer>();
		ArrayList<Integer> mod2 = new ArrayList<Integer>();
		int sum = 0;
		for(int i=0 ; i<n ; i++){
			nums.add(scan.nextInt());
			if(nums.get(i)%3==1)
				mod1.add(nums.get(i));
			else if(nums.get(i)%3==2)
				mod2.add(nums.get(i));
			sum += nums.get(i);
		}
		Collections.sort(nums);
		Collections.sort(mod1);
		Collections.sort(mod2);
		if(nums.get(0)!=0){
			System.out.println("Not possible");
		}
		else{
			
			if(sum%3==0){
				Collections.reverse(nums);
				for(int j=0 ; j<nums.size() ; j++)
					System.out.print(nums.get(j));
			}
			else if(sum%3==1){
				if(mod1.size()>0){
					nums.remove(mod1.get(0));
				}
				else{
					if(mod2.size()>1){
						nums.remove(mod2.get(0));
						nums.remove(mod2.get(1));
					}
					else{
						System.out.println("Not possible");
					}
				}
				Collections.reverse(nums);
				for(int j=0 ; j<nums.size() ; j++)
					System.out.print(nums.get(j));	
			}
			else if(sum%3==2){
				if(mod2.size()>0){
					nums.remove(mod2.get(0));
				}
				else{
					if(mod1.size()>1){
						nums.remove(mod1.get(0));
						nums.remove(mod1.get(1));
					}
					else{
						System.out.println("Not Possible");
					}
				}
				Collections.reverse(nums);
				for(int j=0 ; j<nums.size() ; j++)
					System.out.print(nums.get(j));
			}
		}		
	}

}
