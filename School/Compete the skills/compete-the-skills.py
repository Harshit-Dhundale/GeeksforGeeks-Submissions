#User function Template for python3
class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb        # Your code goes here
        for i,j in zip(a,b):
            if i>j:
                cc[0]+=1 # initial value of cc = [0,0]
            elif i<j:
                cc[1]+=1
            else:
                cc = cc
        return cc


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	a = [int(x) for x in input().strip().split()]
    	b = [int(x) for x in input().strip().split()]
    	
    	cc = [0, 0]
    	ob=Solution()
    	ob.scores(a, b, cc)
    	print(*cc)
    	
    	T -= 1

if __name__ == "__main__":
    main()







# } Driver Code Ends