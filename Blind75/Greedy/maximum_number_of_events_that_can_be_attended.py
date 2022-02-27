"""
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

Greedy algorithm: sort the events by start time.
Among all the open events, pick the one that ends the earliest.
"""
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[0])
        attendance = 0 
        pq = []
        j = 0
        
        for i in range(1,100001):
            if attendance == len(events):
                return attendance
            #add new events
            while j < len(events) and events[j][0] == i:
                heapq.heappush(pq, (events[j][1], events[j][0]))
                j += 1
            #remove events that has expired and pop the valid node with the earliest end date 
            lastNode = None
            while pq:
                lastNode = heapq.heappop(pq)
                #valid node
                if lastNode[0] >= i:
                    attendance += 1
                    break
            
        return attendance