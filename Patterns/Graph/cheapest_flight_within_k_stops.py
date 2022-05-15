"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/

Dijkstra's algorithm: mimize price
Keep all the solutions with a bit of optimization (eliminate the choice with more stops and higher price)
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # graph: [[(dest, price)]]
        graph = [[] for i in range(n)]
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        
        # minPQ: node-(price, src, stops)
        pq = []
        heapq.heappush(pq, (0, src, 0))
        
        # keep track of the minimum number of stops to get to one node - avoid TLE
        visited = [float("inf") for i in range(n)]
        
        while pq:
            price, src, stops = heapq.heappop(pq)
            if src == dst:
                return price
            if visited[src] <= stops:
                continue
            visited[src] = stops
            for neighbour in graph[src]:
                # not >= !
                if stops > k:
                    continue
                heapq.heappush(pq, (price+neighbour[1], neighbour[0], stops+1))
        
        return -1