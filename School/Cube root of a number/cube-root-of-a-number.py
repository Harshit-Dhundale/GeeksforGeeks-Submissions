#User function Template for python3
class Solution:
    def cubeRoot(self, N):
        # code here 
        
        l = 0
        
        r = N
        
        res = 0
        
        while l <=r:
            
            m = (l+r)//2
            
            target = m*m*m
            
            
            if target == N:
                
                return target
                
            elif target < N:
                
                res = m
                
                l = m+1
                
            else:
                
                r = m-1
                
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.cubeRoot(N))
# } Driver Code Ends