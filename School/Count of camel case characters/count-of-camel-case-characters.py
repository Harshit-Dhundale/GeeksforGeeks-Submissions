#User function Template for python3
import re
class Solution:
    def countCamelCase (self,s):
        # your code here
        
        return len(re.findall(r"[A-Z]", s))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends