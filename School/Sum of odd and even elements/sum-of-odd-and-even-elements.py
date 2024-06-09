#User function Template for python3
class Solution:
    def find_sum(self, n):
        # Code here
        total=int(n*(n+1)//2)
        s=(n+1)/2
        odd=int(s)**2
        even=total-odd
        return(odd,even)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.find_sum(n)
		for _ in ans:
			print(_, end=" ")
		print()
# } Driver Code Ends