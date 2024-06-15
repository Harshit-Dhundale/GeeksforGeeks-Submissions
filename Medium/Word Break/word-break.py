#User function Template for python3

class Solution:
   def wordBreak(self, n, s, dic):
        if len(s)==0:
            return True
        l=len(s)
        for i in range(1,l+1):
            st=s[:i]
            temp=s[i:]
            if st  in dic and self.wordBreak(n,temp,dic):
                return True
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends