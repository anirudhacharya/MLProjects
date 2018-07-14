package competition;
import java.util.ArrayList;
import java.util.Scanner;

public class Numbers{
    public static void main(String[] args){
        Scanner console = new Scanner(System.in);
        int T = Integer.parseInt(console.nextLine());
        
        for(int i=0 ; i<T ; i++){
        	ArrayList<Integer> B = new ArrayList<Integer>();
            ArrayList<Integer> A = new ArrayList<Integer>();
            int N = Integer.parseInt(console.nextLine());
            String[] in = console.nextLine().split(" ");
            for(int j=0 ; j<in.length ; j++){
            	A.add(Integer.parseInt(in[j]));
            }
            B.add(A.get(0));
            for(int j=1 ; j<N ; j++){
                B.add(lcm(A.get(j-1),A.get(j)));
            }
            B.add(A.get(N-1));
            String out = "";
            for(int j=0 ; j<B.size() ; j++){
                out = out + B.get(j) + " ";
            }
            System.out.println(out.trim());
        }
    }
    
    public static int lcm(int a, int b){
        int i=1;
        while(true){
            if((a*i)%b==0){
                return a*i;
            }
            else{
                i++;
            }
        }
    }
}