#User function Template for python3

import math

class Solution:
    def floorSqrt(self, x):
        temp=math.sqrt(x)
        return math.floor(temp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends