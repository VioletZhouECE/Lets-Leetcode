"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""
class Solution:
    """
    DFS + Memoization:
    Construct a graph
    Do a dfs (without the visited set since we need to explore all increasing paths)

    Keys:
    1. memoization - maxPaths to store the maximum path starting from an index.
    2. dirs = [(0,1), (0,-1), (1,0), (-1,0)] helps you traverse the grid
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #common technique to traverse right, left, top, bottom cell
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(row, col):
            longestPath = 0
            for d in dirs:
                x, y = row+d[0], col+d[1]
                if x<0 or x>len(matrix)-1 or y<0 or y>len(matrix[0])-1:
                    continue
                if matrix[x][y] > matrix[row][col]:
                    if maxPaths[x][y] != 0:
                        longestPath = max(longestPath, maxPaths[x][y])
                    else:
                        longestPath = max(longestPath, dfs(x,y))
            maxPaths[row][col] = 1+longestPath
            return 1+longestPath
        
        longestPath = 0
        maxPaths = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                longestPath = max(longestPath, dfs(i, j))
        
        return longestPath

    """
    Topological sort:
    Construct the graph such that a->b if b > a:
    The longest increasing path = the longest path in a unweighted DAG
    Use kahn's algorithm to find the longest path a unweighted DAG
    Runtime: O(nm)

    Why do we need to use kahn's algorithm?
    If we compute the topological ordering of nodes with DFS, the topological ordering alone does not tell us what the starting nodes are.
    We need the starting nodes to compute the longest path (recall this is not necessarily a connected graph)
    """
    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        indegree = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                for d in dirs:
                    x, y = r+d[0], c+d[1]
                    if x<0 or y<0 or x>len(matrix)-1 or y>len(matrix[0])-1:
                        continue
                    #there's an edge from (r,c) to (x,y)
                    if matrix[x][y] > matrix[r][c]:
                        indegree[x][y] += 1
                        
        queue = deque()
        
        #find the starting node(s) whose indegree = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if indegree[r][c] == 0:
                    queue.append((r,c))
        
        #kahn's algorithm
        maxPath = 0
        while queue:
            size = len(queue)
            for i in range(size):
                r,c = queue.popleft()
                for d in dirs:
                    x, y = r+d[0], c+d[1]
                    if x<0 or y<0 or x>len(matrix)-1 or y>len(matrix[0])-1:
                        continue
                    #there's an edge from (r,c) to (x,y)
                    if matrix[x][y] > matrix[r][c]:
                        indegree[x][y] -= 1
                        if indegree[x][y] == 0:
                            queue.append((x,y))
            maxPath += 1
        
        return maxPath