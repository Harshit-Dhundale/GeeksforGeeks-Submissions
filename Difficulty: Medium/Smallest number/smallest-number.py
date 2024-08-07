#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def smallestNumber(self, s, d):
        def sums(n):
            ans = 0
            while n > 0:
                ans += (n%10)
                n = n //10
            return ans
        minim = 10**(d-1)
        maxm = 10**d
        for i in range(minim, maxm):
            if s == sums(i):
                return i
        return -1

#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends