#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        return max(min(q, 2 * (n + 1) - q) - 1, 0)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends