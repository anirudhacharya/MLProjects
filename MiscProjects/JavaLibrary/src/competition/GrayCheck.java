package competition;
// IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
// SOME CLASSES WITHIN A PACKAGE MAY BE RESTRICTED
// DEFINE ANY CLASS AND METHOD NEEDED
// CLASS BEGINS, THIS CLASS IS REQUIRED
public class GrayCheck
{
 //METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
 public static int grayCheck(byte term1, byte term2){
  // INSERT YOUR CODE HERE
  /*
  My approach is to XOR the two numbers. 
  If they are gray code sequences then the numbers will differ by just one bit
  and when XORed the result will be that one bit which is different in the two numbers.
  We then count the number of set bits in the result. If it is equal to 1 then we 
  return that the two given numbers are gray code sequences, else we return it is not.
  
  M
  */
	 int result = term1 ^ term2;
	 int numOfBits = Integer.bitCount(result);
	 if (numOfBits==1){
		 return 1;
	 }
	 else{
		 int result1 = term1 & term2;
		 if (result1==term1||result1==term2)
			 return 1;
		 else
			 return 0;
	 }
 }
// METHOD SIGNATURE ENDS

// DO NOT IMPLEMENT THE main( ) METHOD
 public static void main(String[] args) 
 {
      // PLEASE DO NOT MODIFY THIS FUNCTION
      // YOUR FUNCTION SHALL BE AUTOMATICALLY CALLED AND THE INPUTS FROM HERE SHALL BE PASSED TO IT
      byte term1=(byte)11110111,term2=(byte)11110101;
      int out;
      // ASSUME INPUTS HAVE ALREADY BEEN TAKEN
      out = grayCheck(term1,term2);
      System.out.println(out);
      //Print the output
 }
}