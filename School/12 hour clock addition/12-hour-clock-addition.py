#User function Template for python3
class Solution:
    def clockSum(self, num1, num2):
        # code here
        hours = [i for i in range(0,12,1)]
        s = (num1+num2)
        if abs(s) >= 12:
            s = s%12
        return hours[s]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1, num2 = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.clockSum(num1, num2))

# } Driver Code Ends