"""
https://leetcode.com/problems/non-overlapping-intervals/

Optimization problem where we need to make a series of choices to minimize the number of intervals to remove.
Greedy (you immediately know what is the best choice) or DP (we make the choice based on previously computed information).

A greedy solution: 
Sort the intervals by end time.
If overlap, always remove the interval with a greater end time.

Why?
Suppose that we have two intervals that overlap, removing the second interval always leads to fewer "future conflicts" and is a better choice.
Why? The future intervals are more likely to overlap with the second interval.
If a future interval overlaps with the first interval, it must also overlap with the second interval.
While the reverse is not true - there could be future intervals that overlap with the second interval but not the first one. 
Thus keeping the first interval leads to fewer "future conflicts".

How to informally "prove" the corretness of a greedy algorithm in an interview?
Argue that the current choice we make is not only the best/optimal choice we can make so far, but it is also optimal for future choices.
In this case, removing the second interval is the best choice we can make so far 
(we have to remove at least one interval of the two intervals), and it is also optimal for the future because it leads to fewer "future conflicts".

Time complexity: O(nlogn). Space complexity: O(1)

This problem can also be solved with DP (non-optimally).
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals, key=lambda x:x[1])
        lastIntervalEnds = sortedIntervals[0][1]
        removedIntervals = 0
        
        for i in range(1,len(sortedIntervals)):
            if sortedIntervals[i][0] >= lastIntervalEnds:
                lastIntervalEnds = sortedIntervals[i][1]
            else:
                removedIntervals += 1
        
        return removedIntervals