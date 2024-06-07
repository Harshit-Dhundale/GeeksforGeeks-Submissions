#User function Template for python3
class Solution:
    def isInRange (ob,N):
        # code here 
        numbers = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
        if int(N) <= 10:
            return numbers[N]
        else:
            return 'not in range'
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.isInRange(N))
# } Driver Code Ends