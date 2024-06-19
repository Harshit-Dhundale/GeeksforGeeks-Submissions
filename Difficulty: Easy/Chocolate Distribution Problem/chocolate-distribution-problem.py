#User function Template for python3
class Solution:

    def findMinDiff(self, A,N,M):
        # code here
        A.sort()
        minimum = float("inf")
        i = 0
        
        while i < N-M+1:
            minimum = min(abs(A[i+M-1] - A[i]), minimum)
            
            i += 1
            
        return minimum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends