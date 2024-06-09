class Solution:
	def sum_of_square_oddNumbers(self, n):
		# Code here
		return ( n * (2*n-1) * (2*n+1) )//3

#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.sum_of_square_oddNumbers(n)
		print(ans)
# } Driver Code Ends