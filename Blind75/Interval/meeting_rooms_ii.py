"""
https://leetcode.com/problems/meeting-rooms-ii/

Key: The minimum number of conference rooms required is determined by the maximum number of meetings that are happening at any given time.
Don't think in terms of intervals (doing stuff with intervals, like finding the overlapping intervals, is hard), think in terms of the the start and the end timestamp.

Time complexity: O(nlogn). Space complexity: O(n)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sortedStartTime = sorted(intervals, key=lambda x:x[0])
        sortedEndTime = sorted(intervals, key=lambda x:x[1])
        maxOverlaps, currOverlaps = 0, 0
        i,j = 0, 0
        
        while i<len(sortedStartTime) and j<len(sortedEndTime):
            if sortedStartTime[i][0] < sortedEndTime[j][1]:
                currOverlaps += 1
                maxOverlaps = max(currOverlaps, maxOverlaps)
                i+=1
            else:
                currOverlaps -= 1
                j+=1
                
        if i<=len(sortedStartTime)-1:
            currOverlaps += len(sortedStartTime)-i
            maxOverlaps = max(currOverlaps, maxOverlaps)
            
        return maxOverlaps
            