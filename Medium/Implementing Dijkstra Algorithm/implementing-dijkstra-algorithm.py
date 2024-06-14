class Solution:
    def dijkstra(self, V, adj, S):
        import heapq
        dist=[float('inf')]*V
        dist[S]=0
        seen=set()
        q=[(0,S,)]
        while q:
            curdist,curnode=heapq.heappop(q)
            if curnode in seen:
                continue
            dist[curnode]=curdist
            seen.add(curnode)
            for nxt,cst in adj[curnode]:
                heapq.heappush(q,(curdist+cst,nxt,))
        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends