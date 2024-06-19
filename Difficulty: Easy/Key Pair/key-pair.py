#User function Template for python3
class Solution:
    def hasArrayTwoCandidates(self,arr, n, x):
        # code here
        seen=set()
        for i in arr:

# Calculate the x-i
            
            if (x-i) in seen :
              return True
            seen.add(i)
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends