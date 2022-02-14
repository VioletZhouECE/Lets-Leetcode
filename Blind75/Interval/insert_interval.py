"""
https://leetcode.com/problems/insert-interval/
"""
class Solution:
    """
    This code looks a bit ugly because we need to handle the case where there is no overlaping intervals separately.
    This is not very elegant.
    """
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

    """
    This is a lot cleaner :)
    For loop gives a nicer pattern than two while loops
    Also being able to continously merge is nice :)
    """
    def insert_clean(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                return res + [newInterval] + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        #if the newly inserted interval should be the last interval
        return res + [newInterval]