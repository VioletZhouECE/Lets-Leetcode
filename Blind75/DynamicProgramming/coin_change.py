"""
https://leetcode.com/problems/coin-change/

Recurrence relation:
coinChangeHelper(n) = min(coinChangeHelper(n-1), coinChangeHelper(n-2), coinChangeHelper(n-5)) + 1

DP:
Initial array: [0,inf,inf,inf,inf,...]
Final array:   [0,1,1,2,2,1,2,2,...]

Note: 
1. An edge case is when amount is 0. Be sure to test this.
2. Use inf to indicate that a amount is impossible - it takes infinite steps to make up that amount. This enables the code to "eliminate" the choice since it always pick the minimum value:
    minCoins[i] = min(minCoins[i], inf+1) -> minCoins will be set to inf
    
m - number of coins, n - the total amount
Time complexity: O(mn). Space complexity: O(n)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [float("inf")]*(amount+1)
        minCoins[0] = 0
            
        i=1
        while i<amount+1:
            if i in coins:
                minCoins[i] = 1
            else:
                #explore all the choices and find the best one
                for coin in coins:
                    if i-coin>=0:
                        minCoins[i] = min(minCoins[i], minCoins[i-coin]+1)
            i += 1
            
        if minCoins[-1] == float("inf"):
            return -1
        return minCoins[-1]