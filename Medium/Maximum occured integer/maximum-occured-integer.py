#User function Template for python3
class Solution:
    def maxOccured(self, n, l, r, maxx):
        arr = [0] * (maxx + 2)
        for i in range(n):
            arr[l[i]] += 1
            arr[r[i] + 1] -= 1
            
        for i in range(1, maxx + 1):
            arr[i] += arr[i - 1]
            
        maxi, num = 0, -1
        for i in range(0, maxx + 1):
            if arr[i] > maxi:
                maxi = arr[i]
                num = i
            elif arr[i] == maxi:
                num = min(num, i)
                
        return num
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends