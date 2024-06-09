#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def relationalOperators(self, A, B):
        # code here
        if A<B:
            print("{} is less than {}".format(A, B))
        elif A>B:
            print("{} is greater than {}".format(A, B))
        else:
            print("{} is equal to {}".format(A, B))

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        A, B = map(int,input().strip().split())
        obj = Solution()
        obj.relationalOperators(A, B)
# } Driver Code Ends