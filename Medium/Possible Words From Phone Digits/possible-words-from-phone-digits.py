#User function Template for python3


class Solution:
    
  def possibleWords(self,a,N):
        #Your code here
        if N == 0:
            return []

        # Define the keypad mapping
        keypad = {
            0: "",
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        # Function to generate words recursively
        def generate_words(curr_word, digits):
            if not digits:
                res.append(curr_word)
                return

            digit = digits[0]
            letters = keypad[digit]

            for letter in letters:
                generate_words(curr_word + letter, digits[1:])

        res = []
        generate_words("", a)
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends