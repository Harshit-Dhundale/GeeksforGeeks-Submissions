#User function Template for python3
class Solution:
	def CountWays(self, str):
		# Code here
		
		
		if str[0] == "0"  or "00" in str:
		    
		    return 0
		
		ln = len(str)
		
		dp = [0]*(ln+1)
		
		dp[0] = 1
		
		dp[1] = 1
		
		mod = 10**9 + 7
		
	
		
		
		for i in range(2, ln+1):
		    
		    
		    if str[i-1] != "0":
		        
		        dp[i] = dp[i-1]
		        
		    if str[i-2] == "1" or (str[i-2] == "2" and str[i-1] <= "6"):
		        
		        dp[i] += dp[i-2]
		        
		        dp[i] %= mod
		        
		        
		   
		        
		#print(dp)
		        
		        
		return dp[ln]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends