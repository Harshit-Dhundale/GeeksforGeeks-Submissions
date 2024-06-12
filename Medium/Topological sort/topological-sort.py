class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        adj_map = self.adjList_to_adjMap(adj, V)
        stack = []
        visited = [False]*V
        for i in range(V):
            if not visited[i]:
                self.dfs(i,adj_map,stack,visited)
        return stack[::-1]
        
    def dfs(self,node,adj_map,stack,visited):
        visited[node] = True
        for neighbor in adj_map.get(node, []):  # Use get to handle empty lists
            if not visited[neighbor]:
                self.dfs(neighbor,adj_map,stack,visited)
                
        stack.append(node)    
    
    def adjList_to_adjMap(self,adj, V):
        adj_map = {}
        for i in range(V):
            adj_map[i] = adj[i]
        
        return adj_map
#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends