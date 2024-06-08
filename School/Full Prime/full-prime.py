#User function Template for python3
class Solution:
    def fullPrime(self,N):
        #code here
        def is_prime(n):
            if n==1 or n==0:
                return False
            for i in range(2, int(n**0.5+1)):
                if n%i==0:
                    return False
            return True
        
        if is_prime(N):
            while N>0:
                if is_prime(N%10):
                    pass
                else:
                    return 0
                N//=10
        else:
            return 0
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.fullPrime(N))
# } Driver Code Ends