#User function Template for python3
class Solution:
    def printUnsorted(self,arr, n):
    
     # code here
    
            lis=arr.copy()
    
            lis.sort()
    
            if n==1:
    
                return (0,0)
    
                
    
            for i in range(n):
    
                if lis[i]!=arr[i]:
    
                    k=i
    
                    break
    
            for j in range(n-1,-1,-1):
    
                if lis[j]!=arr[j]:
    
                    k1=j
    
                    break
    
     
    
            return k,k1   
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printUnsorted(arr, n)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends