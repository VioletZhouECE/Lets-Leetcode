"""
https://leetcode.com/problems/unique-paths-ii/
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
            return 0
        numOfPaths = [[-1 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        return self.uniquePathsWithObstaclesHelper(obstacleGrid, 0, 0, numOfPaths)
        
    def uniquePathsWithObstaclesHelper(self, obstacleGrid, row, col, numOfPaths):
        numRows = len(obstacleGrid)
        numCols = len(obstacleGrid[0])
        if row == numRows-1 and col == numCols-1:
            return 1
        
        dirs = [(1,0), (0,1)]
        totalNumofPaths = 0
        for direction in dirs:
            newRow, newCol = row + direction[0], col + direction[1]
            if newRow < 0 or newRow > numRows-1 or newCol < 0 or newCol > numCols-1:
                continue
            if obstacleGrid[newRow][newCol] == 1:
                continue
            if numOfPaths[newRow][newCol] != -1:
                totalNumofPaths += numOfPaths[newRow][newCol]
            else:
                totalNumofPaths += self.uniquePathsWithObstaclesHelper(obstacleGrid, newRow, newCol, numOfPaths)
            
        numOfPaths[row][col] = totalNumofPaths
        return totalNumofPaths