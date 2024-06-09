#User function Template for python3
class Solution:
    def subClock(self, num1, num2):
        # code here
        hours = [i for i in range(0,12,1)]
        s = (num1-num2)
        if abs(s) >= 12:
            s = s%12
        return hours[s]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1,num2=map(int,input().split())
        
        ob = Solution()
        print(ob.subClock(num1,num2))
# } Driver Code Ends