//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String S[] = read.readLine().split(" ");
            
            Long a = Long.parseLong(S[0]);
            Long b = Long.parseLong(S[1]);
            Long x = Long.parseLong(S[2]);
            
            Solution ob = new Solution();
            System.out.println(ob.canReach(a,b,x));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    static int canReach(Long a, Long b, Long x) {
        
        long dist_remain = Math.abs(a)+Math.abs(b)-3;
        long steps_diff = x-dist_remain;
        
        if(steps_diff<0 || steps_diff%2==0 || x<0) return 0;
        
        else return 1;
    }

};