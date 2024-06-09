#User function Template for python3
class Solution:
    
    def isPerfect(self,N):
        # step1: Sum of factorials of digits
        n = N
        s = 0
        while n>0:
            digit = n%10
            f = Solution.factorial(digit)
            s+=f
            n = n//10
        
        # step2: is perfact or not
        return 1 if s==N else 0
        
    # static method
    def factorial(n):
        if n==1 or n==0:
            return 1
        else:
            return n*Solution.factorial(n-1)   #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isPerfect(N))   
# } Driver Code Ends