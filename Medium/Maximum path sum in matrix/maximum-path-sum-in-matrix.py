#User function Template for python3
class Solution:
    def maximumPath(self, N, mat):
        # code here
        li=[]
        li.append(mat[0])
        for i in range(1,N):
            li.append([])
            for j in range(N):
                li[i].append(0)
        for i in range(1,N):
            for j in range(N):
                
                if j-1>=0:
                    li[i][j]=mat[i][j]+li[i-1][j-1]
                if j+1<N:
                    li[i][j]=max(li[i][j],mat[i][j]+li[i-1][j+1])
                li[i][j]=max(li[i][j],mat[i][j]+li[i-1][j])
        return max(li[N-1])



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends