#User function Template for python3
class Solution:
    def minManipulation(self, N, S1, S2): 

        for i in S1:

            if i in S2:

                S2=S2.replace(i, '',1) 

        return len(S2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        S1,S2 = input().strip().split()
        ob = Solution()
        ans = ob.minManipulation(N, S1, S2)
        print(ans)
# } Driver Code Ends