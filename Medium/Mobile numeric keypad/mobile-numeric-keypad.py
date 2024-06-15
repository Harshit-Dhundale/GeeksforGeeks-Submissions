#User function Template for python3
class Solution:
    def getCount(self, n):
        # code here
        if n == 1:
            return 10
            
        #dictionary d - which stores the possible adjacent numbers of each button
        d = {
                0:[0,8],
                1:[1,2,4],
                2:[2,1,3,5],
                3:[3,2,6],
                4:[4,1,5,7],
                5:[5,2,4,6,8],
                6:[6,3,5,9],
                7:[7,4,8],
                8:[8,7,5,9,0],
                9:[9,6,8],
                0:[0,8]
            }
            
        #created 2d array where each row represents the rows in table as shown in the image
        #initially every row is zero
        res = []
        for i in range(n+1):
            li = []
            for j in range(10):
                li.append(0)
            res.append(li)
        
        #making every value in first row as 1
        for i in range(10):
            res[1][i] = 1
            
        #here row starts from 2
        cnt = 0
        for i in range(2,n+1):
            for k in range(10): #the numbers from 0 t0 9
                for j in d[k]:  #d[k] represents the value of key k
                    res[i][k] += res[i-1][j] 
        
        #returning the last row sum
        return sum(res[-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends