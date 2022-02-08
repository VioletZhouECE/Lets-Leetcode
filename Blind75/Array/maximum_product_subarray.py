"""
https://leetcode.com/problems/maximum-product-subarray/

We need to keep track of both prevMax and prevMin because both 
1. prevMax * nums[i]
2. prevMin * nums[i]
could lead to the maximum product.

This is DP: prevMin and prevMax (subproblems) -> currMax and currMin. It is a bit tricky as we need to cache two things instead of just prevMax.

Note that prevMax does not have to be greater than 0 and prevMin does not have to be smaller than 0. Adding the unnecessary restrition complicates the code (what I did in the first submission ;)

Time complexity: O(n). Space complexity: O(1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMax, prevMin, maxProd = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            currMax = prevMax
            prevMax = max(prevMax*nums[i], prevMin*nums[i], nums[i])
            prevMin = min(currMax*nums[i], prevMin*nums[i], nums[i])
            maxProd = max(prevMax, maxProd)
        
        return maxProd