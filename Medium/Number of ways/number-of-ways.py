#User function Template for python3

class Solution:
   def arrangeTiles(self, N):
       dp=[0]*(N+1)
       if N<4:
           return 1
       for i in range(1,4):
           dp[i]=1
       dp[4]=2
       for i in range(5,N+1):
           dp[i]=dp[i-1]+dp[i-4]
       return dp[N]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.arrangeTiles(N))

# } Driver Code Ends