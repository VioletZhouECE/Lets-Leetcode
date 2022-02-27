"""
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

1->n:
Update the taps that waters the current garden
If the current garden is not watered by the previous tap, pick the tap that has the greatest right bound.

Why not traverse the taps?
Our algorithm is: Among all the taps that can water the current garden, we pick the one that has the greatest right bound. We need to choose from the set of the taps that can water the current garden, and to find that, we need to traverse the gardens and keep a pq of taps.

A similar question:
Maximum Number of Events That Can Be Attended
    Among all open events, we attend the event that ends the earliest
CS 341: Paths with the greatest total happiness

Time complexity: O(nlogn). Space complexity: O(logn)
"""
import heapq

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        #sort the taps by the starting index 
        ranges = [[i-r, i+r] for i, r in enumerate(ranges)]
        ranges = sorted(ranges, key=lambda x: x[0])
        
        availableTaps = []
        numOfTaps = 0
        previousRightBound = 0
        j = 0
        
        #traverse each garden
        for i in range(n):
            #update pq
            #add the tap that starts at i
            while j<len(ranges) and ranges[j][0] <= i:
                #range=0, cannot water garden i
                if ranges[j][1] != i:
                    heapq.heappush(availableTaps, (-ranges[j][1], j))
                j += 1
            #remove the taps that ends at i
            while availableTaps and -availableTaps[0][0] <= i:
                heapq.heappop(availableTaps)
            #no tap can water garden i
            if not availableTaps and previousRightBound <= i:
                return -1
            if previousRightBound <= i:
                previousRightBound = -heapq.heappop(availableTaps)[0]
                numOfTaps += 1 
            
        return numOfTaps