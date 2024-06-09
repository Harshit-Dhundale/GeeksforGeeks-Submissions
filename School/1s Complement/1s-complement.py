#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        return S.replace("0", "x").replace("1", "0").replace("x", "1")

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.onesComplement(S,N))
# } Driver Code Ends