"""
https://leetcode.com/problems/is-graph-bipartite/

The way to color any bipartite graph is to do a BFS
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1 for i in range(len(graph))]
        
        for i in range(len(graph)):
            if colors[i] == -1:
                isBipartite = self.bfs(i, graph, colors)
                if isBipartite is False:
                    return False
        return True
    
    def bfs(self, node, graph, colors):
        queue = deque()
        queue.append(node)
        colors[node] = 1
        color = 0
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for neighbour in graph[node]:
                    if colors[neighbour] == colors[node]:
                        return False
                    if colors[neighbour] != -1:
                        continue
                    colors[neighbour] = color
                    queue.append(neighbour)
            color = 1 if color==0 else 0
        
        return True