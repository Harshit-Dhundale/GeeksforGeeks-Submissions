#User function Template for python3
class Solution:
    def nPr(self, n, r):
        # code here
        def factorial(n):
            if n==1 or n==0:
                return 1
            return n*factorial(n-1)
        
        return factorial(n)//factorial(n-r)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends