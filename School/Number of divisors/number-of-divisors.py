#User function Template for python3

class Solution:
    def count_divisors(self, N):
        n=N
        c = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i == n // i and i % 3 == 0:
                    c += 1
                else:
                    if i % 3 == 0:
                        c += 1
                    if (n // i) % 3 == 0:
                        c += 1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3#Back-end complete function Template for Python 3#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.count_divisors(N))
# } Driver Code Ends