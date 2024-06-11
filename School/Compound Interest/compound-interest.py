#User function Template for python3
class Solution:
    def getCompundInterest(self, P ,T , N , R):
        # code here
        return math.floor(P*((1+(R/(N*100)))**(N*T)))
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        P,T,N,R = map(int,input().split())
        
        ob = Solution()
        print(ob.getCompundInterest(P,T,N,R))
# } Driver Code Ends