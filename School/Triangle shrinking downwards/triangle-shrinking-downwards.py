#User function Template for python3
class Solution:
    def triDownwards(self, S):
        # code here
        result = []
        for i in range(len(S)):
            result.append("."*i+S[i:])
        return "".join(result)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()
        
        ob = Solution()
        ans=ob.triDownwards(S)
        
        for i in range(len(ans)):
            print(ans[i],end="")
            if((i+1)%len(S))==0:
                print()
# } Driver Code Ends