from typing import List

class Solution:
    def sieveOfEratosthenes(self, n: int) -> List[bool]:
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                # Updating all multiples of p to not prime
                for i in range(p * p, n+1, p):
                    is_prime[i] = False
            p += 1
        return is_prime
    
    def getPrimes(self, n: int) -> List[int]:
        if n < 2:
            return [-1, -1]  # No pairs possible for numbers less than 2
        
        # Get all primes up to n using the sieve
        is_prime = self.sieveOfEratosthenes(n)
        
        # Find two primes that sum up to n
        for i in range(2, n+1):
            if is_prime[i] and (n - i) >= 2 and is_prime[n - i]:
                # Ensure i <= n-i to maintain the order
                if i <= n - i:
                    return [i, n - i]
        
        return [-1, -1]

#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends