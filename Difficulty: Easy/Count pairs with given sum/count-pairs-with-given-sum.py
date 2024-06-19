#User function Template for python3
class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        l = 0
        count = 0
        hashMap = {}
        while l < len(arr):
            complement = k - arr[l]
            if complement in hashMap:
                count += hashMap[complement] # frequence of the "complement"
            # store the frequence appearence of arr[l] value in the arr
            hashMap[arr[l]] = hashMap.get(arr[l], 0) + 1
            l += 1
        return (count)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends