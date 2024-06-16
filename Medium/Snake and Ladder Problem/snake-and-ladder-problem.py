# User function Template for Python3
class Solution:
    def minThrow(self, N, arr):
        # code here
        ladders = {}
        snakes  = {}
        
        i = 0
        while i < (N*2):
            if arr[i] < arr[i+1]:
                ladders[arr[i]] = arr[i+1]
            else:
                snakes[arr[i]] = arr[i+1]
            
            i += 2
        
        memo = {}
        def recur(ind):
            if ind == 30:
                return 0
            
            if ind > 30: return float('inf')
            if ind in memo: return memo[ind]
            
            ans = float('inf')
            for i in range(1, 7):
                if ind + i in snakes: continue
                if ind+i in ladders:
                    res = 1 + recur(ladders[ind + i])
                    ans = min(res, ans)
                else:
                    res = 1 + recur(ind + i)
                    ans = min(ans, res)
            
            memo[ind] = ans
            return ans
            
        return recur(1)

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends