"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/

Once you find a pair, remove them immediately
Isn't this the same as Two Sum??
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        frequency = Counter(nums)
        
        numPairs = 0
        for num in nums:
            if k-num in frequency:
                if (k-num == num and frequency[k-num] > 1) \
                or (k-num != num and frequency[num] > 0 and frequency[k-num] > 0):
                    frequency[k-num] -= 1
                    frequency[num] -= 1
                    numPairs += 1
        
        return numPairs