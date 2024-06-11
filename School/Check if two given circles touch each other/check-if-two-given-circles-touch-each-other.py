#User function Template for python3
class Solution:
    def circleTouch(self,X1,Y1,R1,X2,Y2,R2):
        #code here
        distance = ((X1-X2)**2 + (Y1-Y2)**2)**0.5
        return 1 if distance<R1+R2 else 0
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        X1,Y1,R1,X2,Y2,R2=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.circleTouch(X1,Y1,R1,X2,Y2,R2))
# } Driver Code Ends