from queue import Queue

class Pair:
    def __init__(self , r , c , t):
        self.r = r
        self.c = c
        self.t = t
        
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
	    
	    m , n = len(grid) , len(grid[0])
	    visited_arr = [[0]*n for _ in range(m)]
	    queue = Queue()
	    countfresh = 0
	    for i in range(m):
	        for j in range(n):
	           
	            if grid[i][j] == 2:
	                queue.put(Pair(i , j , 0))
	                visited_arr[i][j] = 2
	                
	            elif grid[i][j] == 1:
	                countfresh += 1
	                
	            else:
	                visited_arr[i][j] = 0
	                
	   
	    tm = 0             
	    drow = [-1 , 0 , 1 , 0]
	    dcol = [0 , -1 , 0 , 1]
	    cnt = 0           
	    while queue.queue:
	        
	        curr = queue.get()
	        r , c , t = curr.r , curr.c , curr.t
	        tm = max(tm , t)
	        for i in range(4):
	            nrow = r + drow[i]
	            ncol = c + dcol[i]
	            
	            if 0 <=nrow < m and 0<= ncol < n and visited_arr[nrow][ncol] != 2 and grid[nrow][ncol] == 1:
	                queue.put(Pair(nrow , ncol , t+1))
	                visited_arr[nrow][ncol] = 2
	                cnt += 1
	                
	    if cnt != countfresh:
	        return -1
	        
	    
	    return tm

#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends