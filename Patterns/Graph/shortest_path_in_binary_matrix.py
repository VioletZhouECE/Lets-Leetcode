"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

BFS shortest path
The visited array is not strictly necessary but it makes things more efficient
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        numRows = len(grid)
        numCols = len(grid[0])
        directions = [(1,0),(-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        queue = deque()
        queue.append((0,0))
        steps = 1
        
        while queue:
            size = len(queue)
            for i in range(size):
                row, col = queue.popleft()
                if row==numRows-1 and col==numCols-1:
                    return steps
                for direction in directions:
                    newRow, newCol = direction[0]+row, direction[1]+col
                    if newRow < 0 or newRow > numRows-1 or newCol < 0 or newCol > numCols-1:
                        continue
                    if grid[newRow][newCol] == 1:
                        continue
                    if not visited[newRow][newCol]:
                        visited[newRow][newCol] = True
                        queue.append((newRow, newCol))
            steps += 1
        
        return -1