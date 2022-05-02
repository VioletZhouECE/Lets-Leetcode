"""
https://leetcode.com/problems/contiguous-array/

Prefix sum
Reference: https://www.youtube.com/watch?v=uAGt1QoAoMU

Keys:
1. The prefix sum array gives us an efficient way to determine if a subarray satisfies the constraint (# of 1 == # of 0).
2. By using a hashmap, we can lookup if the first index where a certain sum appears in constant time.

Example:
[1,1,0,1,0,1,1,1]
prefixSum = [1,2,1,2,1,2,3,4]
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = -1
        prefixSum = {}
        # don't forget this, otherwise things like [0,1] will fail
        prefixSum[0] = -1
        currSum = 0
        maxLength = 0
        
        for i, num in enumerate(nums):
            currSum += num
            if currSum in prefixSum:
                maxLength = max(maxLength, i-prefixSum[currSum])
            else:
                prefixSum[currSum] = i
        
        return maxLength