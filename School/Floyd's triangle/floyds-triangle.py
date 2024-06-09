#User function Template for python3
class Solution:
    def printFloydTriangle(self, N):
    	#code here
    	c = 0
    	for i in range(1, N+1):
    	    for j in range(1, i+1):
    	        c+=1
    	        print(c, end=" ")
            print()
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printFloydTriangle(N)
        
# } Driver Code Ends