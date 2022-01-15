"""
https://leetcode.com/problems/coin-change/

Note that solution 2 (BFS) is sigificantly faster than solution 1 (DP)

"""
from collections import deque

class Solution:
    """
    Solution 1: (Top-down) How can I make up this specific amount?
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
    def coinChange1(self, coins: List[int], amount: int) -> int:
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

    """
    Solution 2: (Bottom-up) What amounts can I make up using the coins I have?

    BFS: Instead of thinking about how to make up a specific amount n, we start from the existing coins we have and think about what amounts we can make using these coins.

    Time complexity: Since we have a visited array, we will never visit a node twice, and we never add node>n to the queue (since they are useless). Thus in the worst case, we visit no more than n nodes. , so the time complexity is O(n).

    Why is this better than DP (intuitively)? 
    BFS eliminates the following cases:
    1. Unreachable amount (all the "inf" in the DP array).
    2. Amounts which take more than k steps to reach (where k is the number of steps to reach n)
    In the DP approach we need to solve ALL the subproblems (even the useless ones). BFS eliminates these useless subproblems since it limits the problem space to "all the amounts we can reach with the existing coins with a fewer number of steps". This "bottom-up" way of thinking 
    yields a more efficient algorithm.

    Btw, fewest number of coins -> shortest path to reach a node -> BFS in graph
    """

    def coinChange2(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = [False]*(amount+1)
        levelNodes = deque(coins)
        steps = 1
        
        while levelNodes:
            n = len(levelNodes)
            for _ in range(n):
                node = levelNodes.popleft()
                if node == amount:
                    return steps
                for coin in coins:
                    if node+coin<=amount and not visited[node+coin]:
                        levelNodes.append(node+coin)
                        visited[node+coin] = True
            steps += 1
        
        return -1