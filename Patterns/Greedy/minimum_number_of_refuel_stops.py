"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/

This is a tricky question lmao

Algorithm:
Whever we run out of fuel (cannot reach the next station), pick the stop with the maximum fuel. 
Pick the stop with the maximum fuel until we reach the target.

Why does this work?
The decision we made (pick the stop with the maximum fuel) is always the optimal decision:
1. we have to refuel to get to the next station/target.
2. among all the choices we have, we pick the one that maximize the distance we can travel because we want to refuel as little as possible.
Why do we make refuel decision only when we are unable to reach the next station?
Because we want to maximize the number of available choices we have.

Time complexity: O(nlogn). Space complexity: O(n)
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        numOfStops = 0
        pq = []
        totalFuel = startFuel
        
        for station in stations:
            while totalFuel<station[0]:
                if not pq:
                    return -1
                fuel, start = heapq.heappop(pq)
                totalFuel = totalFuel-fuel
                numOfStops += 1
            heapq.heappush(pq, (-station[1], station[0]))
            
        while totalFuel<target:
            if not pq:
                return -1
            fuel, start = heapq.heappop(pq)
            totalFuel = totalFuel-fuel
            numOfStops += 1
            
        return numOfStops
        