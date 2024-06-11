#User function Template for python3

class Solution:
    def diagonals(self, n):
        return int(n*(n-3)//2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.diagonals(n))
# } Driver Code Ends