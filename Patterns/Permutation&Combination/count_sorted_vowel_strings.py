"""
https://leetcode.com/problems/count-sorted-vowel-strings/
"""
class Solution:
    """
    Subproblem: the number of vowel strings of length n that start at s
    countVowelStringsHelper(n, s) = sum(countVowelStringsHelper(n-1, x) for x in (s,5))
    """
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for i in range(0,5)] for j in range(n+1)]
        for i in range(0,5):
            dp[0][i] = 1
        
        for row in range(n+1):
            for col in range(0,5):
                for start in range(col,5):
                    dp[row][col] += dp[row-1][start]
        
        return dp[n][0]

    """
    Alternatively,
    Subproblem: the number of vowel strings of length n that start at s
    countVowelStringsHelper(n, s) = sum(countVowelStringsHelper(n-1, s) for x in (n, s+1))
    Notice this calculate the same thing as the first subproblem.
    """
    def countVowelStrings2(self, n: int) -> int:
        dp = [[0 for i in range(0,5)] for j in range(n+1)]
        for i in range(0,5):
            dp[0][i] = 1
        for j in range(n+1):
            dp[j][4] = 1
        
        for row in range(1,n+1):
            for col in range(3,-1,-1):
                dp[row][col] = dp[row-1][col] + dp[row][col+1]
        
        return dp[n][0]