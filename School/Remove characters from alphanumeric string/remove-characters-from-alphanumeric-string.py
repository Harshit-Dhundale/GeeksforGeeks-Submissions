#User function Template for python3
import re
class Solution:
	def removeCharacters(self, S):
		# code here
		
		return re.sub(r"\D", "", S)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeCharacters(s)
		
		print(answer)


# } Driver Code Ends