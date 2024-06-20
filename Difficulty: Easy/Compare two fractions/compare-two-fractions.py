#User function Template for python3


class Solution:
    def compareFrac (self, s):
       # code here
       s = s.split(',')
       s[1] = s[1].replace(' ','')
       x1 = s[0].split('/')
       x2 = s[1].split('/')
       ans1 = int(x1[0])/int(x1[1])
       ans2 = int(x2[0])/int(x2[1])
       if ans1 == ans2:
           return 'equal'
       if ans1>ans2:
           return x1[0]+'/'+x1[1]
       return x2[0]+'/'+x2[1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends