#User function Template for python3
class Solution:
    def check (self,s):
        # your code here
        if set(s[0])==set(s):
            return True
            
        else:
            return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    if ob.check (s):
        print ("YES")
    else:
        print ("NO")
        
# Contributed By: Pranay Bansal

# } Driver Code Ends