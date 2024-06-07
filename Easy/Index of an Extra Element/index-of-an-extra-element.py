class Solution:
    def findExtra(self,n,a,b):
        #add code here
        s1=sum(a)
        s2=sum(b)
        v=s1-s2
        return a.index(v)

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends