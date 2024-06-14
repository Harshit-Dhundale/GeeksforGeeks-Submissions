#User function Template for python3
class Solution:
    def solve(self,n : int, a : list, b : int):
        for i in range(len(a)):
            if b in a:
                b=b+b
        return b

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n , b = map(int, input().split())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.solve(n, arr, b))
# } Driver Code Ends