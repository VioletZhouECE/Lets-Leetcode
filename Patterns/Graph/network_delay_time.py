"""
https://leetcode.com/problems/network-delay-time/

The shortest path from k to all the nodes -> dijkstra's algorithm
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #initialize graph, delays, and pq
        graph = defaultdict(list)
        delays = {}
        for time in times:
            graph[time[0]].append((time[1], time[2]))
            delays[time[0]] = float("inf")
            delays[time[1]] = float("inf")
    
        pq = deque()
        pq.append((0, k))
        
        while pq:
            delay, node = pq.popleft()
            #if we can improve the delay
            if delay < delays[node]:
                delays[node] = delay
                for neighbour in graph[node]:
                    pq.append((neighbour[1]+delay, neighbour[0]))
        
        #pick the node with the maximum delay
        maxDelay = float("-inf")
        for node in delays.keys():
            maxDelay = max(maxDelay, delays[node])
           
        #detect unreachable nodes
        if len(delays)<n or maxDelay == float("inf"):
            return -1
        return maxDelay