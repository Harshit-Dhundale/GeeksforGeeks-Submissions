#User function Template for python3
class Solution:
    def numberPattern(self, N):
        # code here
        ans = []
        for i in range(1, N + 1):
            s1 = ''
            s2 = ''
            for j in range(1, i):
                s1 += str(j)
                s2 = str(j) + s2
            ans.append(s1 + str(i) + s2)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        res = ob.numberPattern(N)
        for each in res:
            print(each, end=" ")
        print()
        

# } Driver Code Ends