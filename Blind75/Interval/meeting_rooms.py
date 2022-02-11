"""
https://leetcode.com/problems/meeting-rooms/
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        soredIntervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1,len(soredIntervals)):
            if soredIntervals[i][0] < soredIntervals[i-1][1]:
                return False
        return True