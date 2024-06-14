#User function Template for python3
class Solution:
    def kthDigit(self, A, B, K):
        x=A**B
        y=str(x)
        z=y[::-1]
        return z[K-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B,K = input().split()
        ob = Solution()
        print(ob.kthDigit(int(A),int(B),int(K)))
# } Driver Code Ends