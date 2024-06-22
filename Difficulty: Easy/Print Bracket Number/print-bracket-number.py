#User function Template for python3
class Solution:
	def __init__(self):
        self.st = []
    def empty(self):
        return self.st ==[]
    def push(self , ele):
        self.st.append(ele)
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.st.pop()
    def bracketNumbers(self, S):
        ans =  []
        c = 0
        for i in range(len(S)):
            if self.empty() and S[i] == '(':
                c +=1
                ans.append(c)
                self.push(c)
            elif S[i] == '(':
                c +=1
                ans.append(c)
                self.push(c)
            elif S[i].isalpha():
                continue
            else:
                ele = self.st[-1]
                ans.append(ele)
                self.pop()
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends