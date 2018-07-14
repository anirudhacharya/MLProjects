package competition;

import java.util.ArrayList;

public class Solution {
    public ArrayList<Integer> flip(String A) {
        char[] bitStr = A.toCharArray();
        int max = 0;
        int L = 0;
        int R = 0;
        int first = 0;
        int last = 0;
        int cur = 0;
        while (last<A.length()) {
            if (bitStr[last] == '0') {
                cur++;
                if (cur>max) {
                    max = cur;
                    L = first;
                    R = last;
                }
                last++;
            } else {
                cur--;
                if (cur<=0) {
                    cur = 0;
                    last++;
                    first = last;
                    continue;
                }
                last++;
            }
        }
        if (max==0) {
            return new ArrayList<Integer>();
        } else {
            ArrayList<Integer> nums = new ArrayList<Integer>();
            nums.add(L);
            nums.add(R);
            return nums;
        }
    }
}
