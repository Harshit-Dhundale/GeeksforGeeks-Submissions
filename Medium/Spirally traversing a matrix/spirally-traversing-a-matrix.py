#User function Template for python3
class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,mat, r, c): 
        # code here 
        
        t = 0
        
        b = r-1
        
        l = 0
        
        r = c-1
        
        res = []
        
        while t <=b and l <=r:
            
            
            for x in range(l, r+1):
                
                res.append(mat[t][x])
                
                
            t+=1
            
            
            for y in range(t, b+1):
                
                res.append(mat[y][r])
                
                
            r-=1
            
            
            if t <=b:
                
                for x in range(r, l-1, -1):
                    
                    res.append(mat[b][x])
                    
                    
            b-=1
            
            
            if l <=r:
                
                for y in range(b, t-1,-1):
                    
                    res.append(mat[y][l])
                    
                    
            l+=1
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends