#User function Template for python3
class Solution:
    def EvenOddSum(self,N,Arr):
        #code here (return list)
        even = 0
        odd = 0
        for i in range (0,N,2):
            even += Arr[i]
        for j in range(1,N,2):
            odd += Arr[j]
        return [even, odd] 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        ans=ob.EvenOddSum(N,Arr)
        print(ans[0],end=" ")
        print(ans[1])
# } Driver Code Ends