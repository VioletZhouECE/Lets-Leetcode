"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/

Shortest path - BFS
Reference: https://www.youtube.com/watch?v=Vo3OEN2xgwk

Key:
Since we are allowed to visit an edge multiple times, we need to avoid repeating an edge infinitely. We can do this by storing the state - if we go back to a node we visited before without visiting any new node, then we are doing useless work and shouldn't continue. 

The data structure we use is a nested array of size len(graph) * 2^(len(graph)) where 2^(len(graph)) is the number of states: each node has two states: visited and unvisited, and we have len(graph) nodes. We also need to store the state in the queue - using a bitmask instead of a hashset signficantly improve the performance.
"""
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        visited = [[0 for i in range(1<<len(graph))] for j in range(len(graph))]
        queue = deque()
        
        for i, node in enumerate(graph):
            queue.append((i, 1<<i))
        
        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node, state = queue.popleft()
                if state == (1<<len(graph))-1: return steps
                for neighbour in graph[node]:
                    #checking visited before adding neighbours to the queue improves performance
                    if visited[neighbour][state | 1<<neighbour]: continue
                    queue.append((neighbour, state | 1<<neighbour))
                    visited[neighbour][state | 1<<neighbour] = True
            steps+=1
        
        return steps