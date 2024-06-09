#User function Template for python3
class Solution:

    def convert(self, s):
        # code here
        result = ""
        for c in s:
            i = ord(c)
            if 65<=i<=90: # Capital
                result+=chr(65+90-i)
            else:
                result+=chr(97+122-i)
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.convert(s)

        print(ans)
# } Driver Code Ends