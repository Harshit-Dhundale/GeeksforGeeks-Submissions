#User function Template for python3

class Solution:
     def shortestPath(self, s):
        
        ans = ""
        E=s.count('E')
        W=s.count('W')
        N=s.count('N')
        S=s.count('S')
        
        if E > W:   ans += "E"* (E - W)
        if N > S:   ans += "N"* (N - S)
        if S > N:   ans += "S"* (S - N)
        if W > E:   ans += "W"* (W - E)
       
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.shortestPath(s)
        print(ans)
# } Driver Code Ends