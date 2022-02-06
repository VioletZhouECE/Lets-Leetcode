"""
https://leetcode.com/problems/maximum-subarray/

DP:
max(i) = max(i-1)<0? nums[i] : max(i-1)+nums[i]

The key is to notice that the subproblem is the largest sum of nums[:i] (nums[i] HAS TO BE INCLUDED). If we don't include nums[i], it will be difficult to calculate maxSums[i] from maxSums[i-1] as we are not sure if we still have a continuous subarray after including nums[i].
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSums = nums
        
        for i in range(1,len(nums)):
            maxSums[i] = max(maxSums[i-1]+nums[i], nums[i])
            
        return max(maxSums)