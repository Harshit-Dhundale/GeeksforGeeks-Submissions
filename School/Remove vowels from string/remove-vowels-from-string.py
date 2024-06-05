#User function Template for python3
class Solution:
    def removeVowels(self, S):
        ans = ""
        for i in S:
            if i in 'aeiouAEIOU':
                continue
            else:
                ans += i
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeVowels(s)
		
		print(answer)


# } Driver Code Ends