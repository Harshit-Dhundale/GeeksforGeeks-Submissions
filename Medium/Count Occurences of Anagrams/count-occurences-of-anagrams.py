#User function Template for python3
from collections import Counter
class Solution:

	def search(self,pat, txt):
	    window_counter = Counter()
	    pat_counter = Counter(pat)
	    i = count = 0
	    for j, char in enumerate(txt):
	        window_counter[char] += 1
	        
	        if j - i + 1 > len(pat):
	            #decrement if frequency > 1 otherwise delete from hashmap
	            if window_counter[txt[i]] == 1:
	                del window_counter[txt[i]]
	            else:
	                window_counter[txt[i]] -= 1
	            i += 1
	        # check if the current window matches the pattern
	        if window_counter == pat_counter:
                count += 1
        return count
#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends