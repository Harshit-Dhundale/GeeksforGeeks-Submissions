#User function Template for python3
import heapq

class Solution:
    def kthLargest(self, k, arr, n):
        res = []  # To store the Kth largest elements after each insertion
        min_heap = []  # Min-heap to store the K largest elements

        for i in range(n):
            if len(min_heap) < k:
                heapq.heappush(min_heap, arr[i])
            else:
                if min_heap[0] < arr[i]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, arr[i])
            
            if len(min_heap) >= k:
                res.append(min_heap[0])
            else:
                res.append(-1)
        
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        k,n=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(*ob.kthLargest(k,arr,n))
# } Driver Code Ends