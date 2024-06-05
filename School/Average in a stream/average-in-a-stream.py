#User function Template for python3
class Solution:
    def streamAvg(self, arr, n):
        f = 0
        a = []
        # code here
        for i in range(0,n):
            f = f + arr[i]
            k = f/(i+1)
            a.append(k)
            
        return a

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends