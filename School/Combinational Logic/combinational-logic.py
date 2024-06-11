#User function Template for python3

class Solution:
   def logicalOperation (self, A, B, C, D, E, F):
        if ((not A) and B) + (C and D) + (E and (not F)) :
            return 1
        else: return 0   # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B,C,D,E,F = input().split()
        A = int(A)
        B = int(B)
        C = int(C)
        D = int(D)
        E = int(E)
        F = int(F)
        
        ob = Solution()
        print(ob.logicalOperation(A, B, C, D, E, F))
# } Driver Code Ends