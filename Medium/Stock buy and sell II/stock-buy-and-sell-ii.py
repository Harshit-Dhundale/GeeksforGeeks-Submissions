
from typing import List

class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        A = prices
        holding_stock = False
	    stock_bought_price = -1
	    profit = 0
	    
	    i = 0
	    
	    while (i<len(A)):
	        
	        if(i == len(A)-1):
	            if(holding_stock == True):
	                profit += A[i] - stock_bought_price
	        elif(A[i+1] > A[i] and holding_stock == False):
	            holding_stock = True
	            stock_bought_price = A[i]
	        elif(A[i+1] < A[i] and holding_stock == True):
	            holding_stock = False
	            profit += A[i] - stock_bought_price
	            
	        i+=1
	   
	    return profit# code here
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends