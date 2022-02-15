"""
https://leetcode.com/problems/merge-intervals/
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        
        res = []
        for i, interval in enumerate(intervals):
            if res and interval[1] >= res[-1][0] and interval[0] <= res[-1][1]:
                res[-1] = [min(interval[0], res[-1][0]), max(interval[1], res[-1][1])]
            else:
                res.append(interval)
            
        return res