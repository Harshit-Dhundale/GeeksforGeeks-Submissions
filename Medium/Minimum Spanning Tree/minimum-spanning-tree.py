#User function Template for python3
import heapq

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        # using prim's algorithm
        vis=[0]*V
        count=0
        heap=[]
        heapq.heappush(heap,(0,0))
        while heap:
            value=heapq.heappop(heap)
            wt=value[0]
            node=value[1]
            if vis[node]==1:
                continue
            vis[node]=1
            count+=wt
            for i in adj[node]:
                adjnode=i[0]
                weight=i[1]
                if vis[adjnode]!=1:
                    heapq.heappush(heap,(weight, adjnode))
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends