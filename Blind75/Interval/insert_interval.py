"""
https://leetcode.com/problems/insert-interval/

This code looks a bit ugly because we need to handle the case where there is no overlaping intervals separately.
This is not very elegant.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        
        #find the first interval that the newInterval should be merged with
        while left < len(intervals) and intervals[left][1] < newInterval[0]:
            left += 1
        #if we don't need to do any merging
        if left == len(intervals) or intervals[left][0] > newInterval[1]:
            return intervals[0:left] + [newInterval] + intervals[left:]
        startTime = min(newInterval[0], intervals[left][0])
        
        #find the last interval that the newInterval should be merged with
        right = left
        while right < len(intervals)-1 and intervals[right+1][0] <= newInterval[1]:
            right += 1
        endTime = max(newInterval[1], intervals[right][1])
        
        newIntervals = intervals[0:left] + [[startTime, endTime]] + intervals[right+1:]
        
        return newIntervals