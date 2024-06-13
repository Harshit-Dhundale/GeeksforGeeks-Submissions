#User function Template for python3

class Solution:
    
    def getMaxOccurringChar(self,s):
        #get count of all characters
        t={x:s.count(x) for x in list(s)}
        #find the letter with max freq
        m=max(t.values())
        #list of keys with max freq
        l=[ord(x) for x in t.keys() if t[x]==m]
        #return letter with minimum lexicography
        return chr(min(l))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(Solution().getMaxOccurringChar(s))
# } Driver Code Ends