//{ Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        Scanner scn = new Scanner(System.in);
        int t = scn.nextInt();
        while(t-- > 0)
        {
            int N = scn.nextInt();

            Solution ob = new Solution();
            ArrayList<Integer> sum = ob.getSum(N);
            System.out.println(sum.get(0)+" "+sum.get(1));
        }
    }
}

// } Driver Code Ends


//User function Template for Java
class Solution{
    static ArrayList<Integer> getSum(int N){
        // code here
        ArrayList<Integer> result = new ArrayList<>();
        
        Integer oddsum;
        Integer evensum;
        
        Integer totalsum = N*(N+1)/2;
        // if N is even
        if (N%2==0){
            Integer n = N/2;
            oddsum = n*n;
        }
        else{
            Integer n = (N+1)/2;
            oddsum = n*n;
        }
        evensum = totalsum-oddsum;
        
        result.add(evensum);
        result.add(oddsum);
        
        return result;
    }

}