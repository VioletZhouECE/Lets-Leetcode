"""
https://leetcode.com/problems/champagne-tower/

Mathematic relationships can be expressed in a recursive manner :)

Is this faster than recursion with memoization?
No. DP uses an equal amount of space and also computes many subproblems we don't need to solve.
"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for j in range(query_row+1)] for i in range(query_row+1)]
        dp[0][0] = poured
        
        for row in range(1,query_row+1):
            for col in range(row+1):
                if col == 0:
                    dp[row][col] = max(0, dp[row-1][col]-1)/2
                else:
                    dp[row][col] = max(0, dp[row-1][col-1]-1)/2 + max(0, dp[row-1][col]-1)/2
        
        return min(1.0, dp[query_row][query_glass])
        