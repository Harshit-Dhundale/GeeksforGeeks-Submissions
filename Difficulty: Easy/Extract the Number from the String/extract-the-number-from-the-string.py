class Solution:
    def ExtractNumber(self,sentence):
        #code here
        s=sentence.split(' ')
        maxi=-1
        for i in s:
            if i.isdigit():
                if '9' not in i:
                    if int(i)>maxi:
                        maxi=int(i)
                    
        return maxi

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends