"""
https://leetcode.com/problems/critical-connections-in-a-network/

CS 341 moment
Good pratice for recursion!

Bridge: An edge (u,v) is a bridge if low(v) > disc(u), meaning that none of nodes in u's subgraph is connected to an ancestor of u.
In other words, the smallest disc time of the nodes that u's subgraph is connected to is greater than u's disc time.
The key is to calculate the smallest disc time of a subgraph and update it.

Reference: https://www.youtube.com/watch?v=Rhxs4k6DyMM&t=0s
"""
class Solution:
    def __init__(self):
        self.time = 0
        
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])
        disc, low, parent = [-1 for i in range(n)], [None for i in range(n)], [None for i in range(n)]
        bridges = []
        
        for i in range(n):
            if disc[i] == -1:
                self.dfs(i, graph, disc, low, parent, bridges)
            
        return bridges
    
    #compute disc, low, and find all bridges in this subgraph starting at node
    def dfs(self, node, graph, disc, low, parent, bridges):
        disc[node] = self.time
        low[node] = self.time
        self.time += 1
        for neighbour in graph[node]:
            #children
            if disc[neighbour] == -1:
                parent[neighbour] = node
                self.dfs(neighbour, graph, disc, low, parent, bridges)
                low[node] = min(low[node], low[neighbour])
                if low[neighbour] > disc[node]:
                    bridges.append((node, neighbour))
            elif parent[node] != neighbour:
                #ancestor - not direct parent
                low[node] = min(low[node], disc[neighbour])