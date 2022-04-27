"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

construct a graph
do a dfs (without the visited set since we need to explore all increasing paths)

Keys:
1. memoization - maxPaths to store the maximum path starting from an index.
2. dirs = [(0,1), (0,-1), (1,0), (-1,0)] helps you traverse the grid
"""
class Solution:
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