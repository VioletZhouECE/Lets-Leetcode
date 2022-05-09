"""
https://leetcode.com/problems/continuous-subarray-sum/

Prefix sum: _a__b_
All subarrays can be created by chopping of prefixes (prefixSum[0] = -1 allows us to choose not to chop off any prefix). 
In a prefix sum problem, we know exactly what we want to chop off/subtract - all the subarrays satisfy the condition if and only if the prefix ...
What we want to chop off: a%k = (a+b)%k => (a+b)%k - a%k = b%k = 0 => b is a multiple of k.
An additional constraint in this question is that the array needs to have size >= 2. So we keep the smallest index (to maximize the size), and check the size,
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = {}
        #if currSum is a multiple of k, then we don't need to chop off any prefix
        #test this with [0] and [0,0]
        prefixSum[0] = -1
        currSum = 0
        
        for i, num in enumerate(nums):
            currSum += num
            if currSum%k in prefixSum:
                if i-prefixSum[currSum%k] > 1:
                    return True
            else:
                prefixSum[currSum%k] = i
        
        return False