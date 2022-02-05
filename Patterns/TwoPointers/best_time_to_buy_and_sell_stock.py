"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Two pointers
The key is:
    if profit < 0:
        left = right
We can skip all the days between left and right because they are bigger than prices[left] and buying at any day between between left and right will not make the result any better. The only chance that we can get a better result is when we buy at a lower price (prices[right]).

Aside: This is kinda like sliding window, where we reason that the starting points that we skip are not gonna give us a better result. "Skipping" checks allow us to never move the pointer backward.

TL'DR: Always try to buy at a lower price.

Time complexity: O(n). Space complexity: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, maxDiff = 0, 0, 0
        while right < len(prices):
            profit = prices[right]-prices[left]
            if profit < 0:
                left = right
            else:
                maxDiff = max(maxDiff, profit)
            right += 1
        return maxDiff