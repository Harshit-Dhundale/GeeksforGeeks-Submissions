#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
		# code here
		
		
		
		arr[:] = [n2 if n1 > n2 else -1 for n1, n2 in zip(arr,arr[1:])] + [-1]
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends