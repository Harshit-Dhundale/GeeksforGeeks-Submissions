#User function Template for python3
class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        d = {1: 1, 2: 2}
        
        def f_c(n):
            if n in d:
                return d[n]

            result = f_c(n-1) + f_c(n-2)
            
            d[n] = result
            
            return result
            
        return f_c(n)%1000000007

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends