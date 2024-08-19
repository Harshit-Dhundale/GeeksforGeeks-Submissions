#User function Template for python3

class Solution:

    def kthSmallest(self, arr,k):
        
        maxx = max(arr)
        ans = [0]*(maxx+1)
        
        for a in arr:
            ans[a] += 1
            
        for i in range(1, maxx+1):
            
            k -= ans[i]
            
            if k == 0:
                return i
                
        return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends