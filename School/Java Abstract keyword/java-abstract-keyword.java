//{ Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.Scanner;
abstract class A 
{
    int prod;
    abstract void m1(int p,int q);
    void m2()
    {
        System.out.println(prod);
    }
}

public class AbstractDemo 
{
    public static void main(String args[]) 
    {
        Scanner sc=new Scanner (System.in);
        int t=sc.nextInt();
        while(t-->0)
        {
        int a1=sc.nextInt();
        int a2=sc.nextInt();
        B b = new B();
        b.m1(a1,a2);
        b.m2();
        }
    }
}

// } Driver Code Ends
//User function Template for Java
class B extends A 
{   int ans;
    void m1(int p,int q) {
       // Add your code here.
       ans=p*q;
       System.out.println(ans);
    }
    void m2(){
        
    }
}

//{ Driver Code Starts.

// } Driver Code Ends