#User function Template for python3

class Solution:
 def count (self,s):
        up_num=0
        l_num=0
        sp_char=0
        num_v=0
        for i in s:
            if i.isupper():
                up_num+=1
            elif i.islower():
                l_num+=1
            elif i.isdigit():
                num_v+=1
            else:
                sp_char+=1
        return [up_num,l_num,num_v,sp_char]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends