#User function Template for python3

class Solution:
    def findMaxGuests(self, Entry, Exit, N):
            
            s = []
            for i in range(N):
                s.append((Entry[i], 0))
                s.append((Exit[i], 1))
                
            at = None
            an = 0
            n = 0
            s.sort()
            
            for e, t in s:
                if t == 0:
                    n += 1
                if n > an:
                    an = n
                    at = e
                if t == 1:
                    n -= 1
            return an, at

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        
        N = int(input())

        entry = [int(x) for x in input().split()]
        exit =  [int(x) for x in input().split()]

        solObj = Solution()
        ans = solObj.findMaxGuests(entry, exit, N) 
        print(ans[0],ans[1])
        

# } Driver Code Ends