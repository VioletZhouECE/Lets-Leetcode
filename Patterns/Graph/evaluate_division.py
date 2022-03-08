"""
https://leetcode.com/problems/evaluate-division/

Division result => multiplying weights on the path (notice how it has a transitive nature)
We can model this question as a bi-directional graph: it needs to be directed since a/b is different from b/a, and bi-directional since we want to be able to calculate both.

Time complexity: O(m*n) where m is the number of queries and n is the number of equations
Space complexity: O(n) to store the graph
Note: DFS is O(n) since this graph has O(n) edges(one equation = two edges) and O(n) vertices. 
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #build the graph
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            #bi-directional
            graph[eq[0]].append((eq[1], values[i]))
            graph[eq[1]].append((eq[0], 1/values[i]))
        
        #dfs for each query
        result = []
        for query in queries:
            visited = set()
            ret = self.dfs(query[0], query[1], 1, graph, visited)
            if ret:
                result.append(ret)
            else:
                result.append(-1)
        
        return result
    
    def dfs(self, node, target, result, graph, visited):
        if node not in graph:
            return None
        if node == target:
            return result
        visited.add(node)
        for neighbour, val in graph[node]:
            if neighbour not in visited:
                ret = self.dfs(neighbour, target, result*val, graph, visited)
                if ret:
                    return ret
        return None