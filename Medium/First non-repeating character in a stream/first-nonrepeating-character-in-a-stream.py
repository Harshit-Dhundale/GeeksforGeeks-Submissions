#User function Template for python3
from collections import deque, defaultdict
class Solution:
    def FirstNonRepeating(self, A):
        q = deque()
        freq = defaultdict(int)
        result = []
    
        # Iterate over each character 
        for ch in A:
            q.append(ch)
            freq[ch] += 1
        
            # Remove characters from the front of the queue until a frequency of 1
            while q and freq[q[0]] > 1:
                q.popleft()
        
            # If the queue is empty, append '#' 
            if not q:
                result.append('#')
            else:
                result.append(q[0])
    
        return ''.join(result)

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends