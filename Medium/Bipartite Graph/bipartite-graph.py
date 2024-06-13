class Solution:
    def isBipartite(self, V, graph):
        def validcolouring(graph,colour,node,col):
            if colour[node] != 0:
                return colour[node] == col
            colour[node] = col
            for node in graph[node]:
                if not validcolouring(graph,colour,node,-col):
                    return False
            return True
        n = len(graph)
        colour = [0]*n
        for node in range(n):
            if colour[node] == 0 and not (validcolouring(graph,colour,node,1)):
                return False
        return True


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends