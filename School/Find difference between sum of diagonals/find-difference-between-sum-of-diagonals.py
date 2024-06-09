#User function Template for python3
class Solution:
    def diagonalSumDifference(self,N,Grid):
        #code here
        lenm = len(Grid)
		
        dig = 0
        digder = 0
        for i in Grid:
            digder += Grid[dig][dig]
            dig += 1
        
        dig= lenm-1
        dig_u = 0
        digizq = 0
        for i in Grid:
            digizq += Grid[dig_u][dig]
            dig -= 1
            dig_u += 1
            
		return abs(digizq-digder)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Grid = [[0 for i in range(N)] for j in range(N)]
        for i in range(N):
            s=list(map(int,input().strip().split(' ')))
            for j in range(N):
                Grid[i][j]=s[j]
        ob=Solution()
        print(ob.diagonalSumDifference(N,Grid))
# } Driver Code Ends