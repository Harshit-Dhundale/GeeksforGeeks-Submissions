#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q = Queue()
        visited_arr  = [False]*V
        q.put(0)
        visited_arr[0] = True
        
        bfs_traversal = []
        
        while q.queue:
            
            vertex = q.get()
            bfs_traversal += [vertex]
            
            if len(adj[vertex]) > 0:
                for neighbour in adj[vertex]:
                    if not visited_arr[neighbour]:
                        q.put(neighbour)
                        visited_arr[neighbour] = True
                    
        return bfs_traversal

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends