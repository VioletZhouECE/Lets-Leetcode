"""
https://leetcode.com/problems/delete-and-earn/

This question is very similar to House Robber.
Basically, if you choose the current number, you cannot choose its neighbours
The only difference is that each number may occur multiple times (this is why you need a hashmap for counting)

Time complexity: O(k). Space: O(k), where k is the maximum number in nums
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxNum = max(nums)
        dp = [0 for i in range(maxNum+1)]
        numCount = Counter(nums)
        dp[1] = numCount[1] if 1 in numCount else 0
        
        for i in range(2,maxNum+1):
            if i in numCount:
                dp[i] = max(numCount[i]*i+dp[i-2], dp[i-1])
            else: 
                dp[i] = dp[i-1]
        
        return dp[-1]