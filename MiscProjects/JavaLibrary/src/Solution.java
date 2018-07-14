import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        int n = in.nextInt();
        String magazine[] = new String[m];
        for (int magazine_i = 0; magazine_i < m; magazine_i++) {
            magazine[magazine_i] = in.next();
        }
        String ransom[] = new String[n];
        for (int ransom_i = 0; ransom_i < n; ransom_i++) {
            ransom[ransom_i] = in.next();
        }
        Map<String, Integer> mag = new HashMap<String, Integer>();
        for (String mgz : magazine) {
            if (mag.containsKey(mgz)) {
                mag.put(mgz, mag.get(mgz) + 1);
            } else {
                mag.put(mgz, 1);
            }
        }
        boolean flag = true;
        for (String rsm : ransom) {
            if (mag.containsKey(rsm)) {
                if (mag.get(rsm) > 0) {
                    mag.put(rsm, mag.get(rsm) - 1);
                } else {
                    flag = false;
                    break;
                }
            } else {
                flag = false;
                break;
            }
        }
        if (flag) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
