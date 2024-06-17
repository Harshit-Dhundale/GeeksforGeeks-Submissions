#User function Template for python3
class Solution:
    def kadane(self, ans):
        cur_sum = 0 
        best_sum = float('-inf')
        
        for val in ans:
            if cur_sum <= 0 :
                cur_sum = val
            else:
                cur_sum += val
                
            best_sum = max(best_sum, cur_sum)
        return best_sum
            
    def maximumSumRectangle(self, R, C, M):
        maxVal = float('-inf')
        
        for i in range(R):
            ans= [0] * C
            for j in range(i, R):
                
                for elem in range(C):
                    ans[elem] += M[j][elem]

                maxVal = max(maxVal, self.kadane(ans))

        return maxVal

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
# } Driver Code Ends