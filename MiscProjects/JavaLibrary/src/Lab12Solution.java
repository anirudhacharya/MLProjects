/*---------------------------------------------------------------------------
// AUTHOR:      	(Put your name here)
// FILENAME:    	Lab12.java
// SPECIFICATION: 	This program introduces 2-d arrays.
// INSTRUCTIONS:  	Read the following code skeleton and add your own code
//          		according to the comments.  Ask your TA or your class-
//          		mates for help and/or clarification.  When you see
//          		//--> that is where you need to add code.
// LAB LETTER:		(Put your Lab Letter here)
//-------------------------------------------------------------------------*/

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Lab12Solution {

	public static void main(String[] args) throws FileNotFoundException {
		
		/*
		 * This lab exercise is about reading a table of numbers from a text file and storing it in a 2-d array
		 * Then you calculate the column-wise sum of table of numbers and then print it out onto the console.
		 */
		
		// Declare Scanner class for reading from the file
		Scanner scan = new Scanner(new File("E:\\Dev\\Java\\Workspace\\JavaLibrary\\src\\Input.txt"));
		
		// Define the 2-d array with dimensions 10x5
		int[][] numTable = new int[10][5];
		
		//Read from the file into the above 2-d array
		for(int i=0 ; i<10 ; i++){
			for(int j=0 ; j<5 ; j++){
				numTable[i][j] = scan.nextInt();
			}
		}
		
		//Finding the column-wise sum of the 2-d array
		int[] sum = new int[5];
		for(int i=0 ; i<10 ; i++){
			for(int j=0 ; j<5 ; j++){
				sum[j] += numTable[i][j];
			}
		}
		
		// Print the sum
		for(int i=0 ; i<5 ; i++){
			System.out.print(sum[i]+" ");
		}
	}

}
