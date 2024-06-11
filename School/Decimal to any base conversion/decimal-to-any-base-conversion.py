#User function Template for python3

class Solution:
    def getNumber(self, B, N):
        b=''
        while N>0:
            r=int(N%B)
            if r<10:
                b+=str(r)
            else:
                b+=chr(ord('A')+r-10)
            N=N//B
        b=b[::-1]
        return b



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        B = int(input())
        N = int(input())
        ob = Solution()
        ans = ob.getNumber(B, N)
        print(ans)
# } Driver Code Ends