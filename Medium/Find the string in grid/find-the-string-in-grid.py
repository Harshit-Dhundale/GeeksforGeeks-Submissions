#User function Template for python3
def search(board,word,row,col,l,a,b):
    if l==len(word):
        return True
    if row>=len(board) or row<0 or col>=len(board[0]) or col<0 or word[l]!=board[row][col]:
        return False
    board[row][col]='@'
    res=search(board,word,row+a,col+b,l+1,a,b)
    board[row][col]=word[l]
    return res
class Solution:
    def searchWord(self, grid, word):
        n=len(grid)
        m=len(grid[0])
        arr=[]
        arr1=[]
        for i in range(n):
            for j in range(m):
                if word[0]==grid[i][j]:
                    if search(grid,word,i,j,0,0,1) or search(grid,word,i,j,0,0,-1) or search(grid,word,i,j,0,1,0) or search(grid,word,i,j,0,1,-1) or search(grid,word,i,j,0,1,1) or search(grid,word,i,j,0,-1,0) or search(grid,word,i,j,0,-1,-1) or search(grid,word,i,j,0,-1,1):
                        arr1.append(i)
                        arr1.append(j)
                        arr.append(arr1)
                        arr1=[]
                        
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends