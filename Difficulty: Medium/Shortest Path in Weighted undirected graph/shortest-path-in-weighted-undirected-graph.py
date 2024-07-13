#User function Template for python3
from collections import deque
import heapq

class Solution:
    def shortestPath(self,n,m,edges):
        adj=[[] for _ in range(n+1)]
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
        parent=[i for i in range(n+1)]
        pq=[(0,1)]
        distances=[float("inf")]*(n+1)
        distances[1]=0
        while pq:
            curr_distance,curr_vertex=heapq.heappop(pq)
            if curr_distance>distances[curr_vertex]:
                continue
            for neighbor,weight in adj[curr_vertex]:
                distance=curr_distance+weight
                if distance<distances[neighbor]:
                    parent[neighbor]=curr_vertex
                    distances[neighbor]=distance
                    heapq.heappush(pq,(distance,neighbor))
        if distances[n]==float("inf"):
            return [-1]
        ans=deque()
        ans.append(n)
        i=n
        while parent[i]!=i:
            i=parent[i]
            ans.appendleft(i)
        ans.appendleft(distances[n])
        return ans

#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends