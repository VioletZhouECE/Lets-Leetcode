"""
This is THE BEST graph question imo.
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
class Solution:
    """
    Dijkstra's algorithm: mimize price
    Keep all the solutions with a bit of optimization (eliminate the choice with more stops and higher price)

    The runtime depends on # of nodes in the pq. 
    Worst-case: O(n^k) - there can't be two node i with the same number of stops due to the pruning we did 
    (if visited[src] <= stops: continue), which only adds the node if it uses fewer stops.
    Time: O(n^k*log(n^k))

    This solution can be improved if a helper array is implemented to make update O(logn) which allows us to do update 
    instead of add. However, it's not very pratical to implement pq in an interview.
    """
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

    """
    Bellman Ford - The optimal solution
    Time: O(m*k)

    Bellman Ford is DP on the number of edges, so naturally it can be used to find the cheapest flight 
    within k stops. For this question, Bellman Ford is better than Dijkstra's.
    """
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for flight in flights:
            if flight[0] not in graph:
                graph[flight[0]] = []
            graph[flight[0]].append((flight[1], flight[2]))
            
        if src not in graph:
            return -1
            
        #initialize DP table
        minCosts = [float("inf") for i in range(n)]
        minCosts[src] = 0
        for neighbour in graph[src]:
            minCosts[neighbour[0]] = neighbour[1]
        
        for i in range(k):
            # Note: make a copy of the prev table to make sure that minCosts[flight[0]] reads the cost with exactly i-1 stops. 
            # Otherwise we might use more than i stops.
            newMinCosts = minCosts.copy()
            for flight in flights:
                newMinCosts[flight[1]] = min(newMinCosts[flight[1]], minCosts[flight[0]]+flight[2])
            minCosts = newMinCosts
    
        if minCosts[dst] == float("inf"):
            return -1
        return minCosts[dst]

    """
    BFS
    The runtime depends on the # of nodes in the queue
    Worst-case: O(n^k) - in every step, we can potentially adds O(n) other nodes to the queue. 
    Pruning doesn't make a difference in terms of the time complexity.
    Time: O(n^k)
    """
    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for flight in flights:
            if flight[0] not in graph:
                graph[flight[0]] = []
            graph[flight[0]].append((flight[1], flight[2]))
            
        minCosts = [float("inf") for i in range(n)]
        queue = deque()
        queue.append((src, 0))
        steps = 0
            
        while queue and steps < k+1:
            size = len(queue)
            for i in range(size):
                node, cost = queue.popleft()
                if node in graph:
                    for neighbour in graph[node]:
                        if cost+neighbour[1] < minCosts[neighbour[0]]:
                            minCosts[neighbour[0]] = cost+neighbour[1]
                            queue.append((neighbour[0], cost+neighbour[1]))
            steps += 1
        
        if minCosts[dst] == float("inf"):
            return -1
        return minCosts[dst]

    """
    DFS - TLE
    Time: O(n^k)
    DFS covers the same set of edges as BFS (every edge that can be reached within k stops of src). 
    It TLE probably because the pruning is less optimal.
    """
    def findCheapestPrice4(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for flight in flights:
            if flight[0] not in graph:
                graph[flight[0]] = []
            graph[flight[0]].append((flight[1], flight[2]))
            
        minCost = float("inf")
        
        def dfs(node, graph, k, dst, cost):
            nonlocal minCost
            if k<0:
                return
            if node==dst:
                minCost = min(minCost, cost)
            if node in graph:
                for neighbour in graph[node]:
                    if cost+neighbour[1] < minCost:
                        dfs(neighbour[0], graph, k-1, dst, cost+neighbour[1])
                        
        
        dfs(src, graph, k+1, dst, 0)
        
        if minCost == float("inf"):
            return -1
        return minCost
