"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

This is the kind of interesting question that doesn't require any specific algo and just require you to think.

Why does this work?
__a__ __b(unsorted)__ __c__
We need to guarantee that:
1. The biggest number in a (peak) is smaller than the smallest number in b; the smallest number in c (valley) is bigger than the biggest number in b.
Once we have nums[curr] < nums[prev], we enter b and need to calculate peak and valley. 
2. a is sorted, b is unsorted, c is sorted.
The first number > valley must be in a sorted array; The last number < peak must be in a sorted array.
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #find the peak and valley
        peak, valley = float("-inf"), float("inf")
        prev = 0
        for curr in range(len(nums)):
            if nums[curr] < nums[prev]:
                peak = max(nums[prev], peak)
                valley = min(nums[curr], valley)
            prev = curr
        if peak == float("-inf") and valley == float("inf"):
            return 0
        
        #find the first number > valley and the last number < peak
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] > valley:
                first = i
                break
        for i in range(len(nums)):
            if nums[len(nums)-1-i] < peak:
                last = len(nums)-1-i
                break
        return last-first+1