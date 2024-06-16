#User function Template for python3


def maxArea(A,le):
    #code here
    
    mn = float("INF")
    
    mx = float("-INF")
    
    for num in A:
        
        mn = min(mn, num)
        
        mx = max(mx, num)
    
    
    l = 0
    
    r = len(A) -1
    
    res = 0
    
    
    while l < r:
        
        hl = A[l]
        
        hr = A[r]
        
        res = max(res,(r-l)*min(hl,hr))
        
        
        if hl < hr:
            
            l+=1
            
        else:
            
            r-=1
     
            
    return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends