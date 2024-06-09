#User function Template for python3
class Solution:
	def DiagonalSum(self, matrix):
		# Code here
        result = 0
        n = len(matrix)
        for i in range(n):
            result+=matrix[i][i]
            result+=matrix[i][n-i-1]
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.DiagonalSum(matrix)
		print(ans)
# } Driver Code Ends