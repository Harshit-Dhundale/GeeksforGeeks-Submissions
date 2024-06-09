#User function Template for python3

class Solution:
    def extractIntegerWords(self, s):
        k=[]
        str1=''
        for i in s:
            if i.isdigit():
                str1+=i
            else:
                if str1:
                    k.append(str1)
                    str1=''
        if str1:
            k.append(str1)
        return k

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        if solObj.extractIntegerWords(s):
            print(*solObj.extractIntegerWords(s))
        else:
            print("No Integers")

# } Driver Code Ends