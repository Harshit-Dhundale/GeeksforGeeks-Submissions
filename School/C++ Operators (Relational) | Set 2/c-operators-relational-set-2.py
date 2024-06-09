#User function Template for python3
class Solution:
    def compareNum(ob,A,B):
        # code here
        if A>B:
            return "{} is greater than {}".format(A, B)
        elif A<B:
            return "{} is less than {}".format(A, B)
        else:
            return "{} is equals to {}".format(A, B)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        A,B=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.compareNum(A,B))
# } Driver Code Ends