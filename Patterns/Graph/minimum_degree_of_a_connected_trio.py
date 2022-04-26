"""
https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

How to check if something is a trio - O(n^3):
Use a nested 3-level for loop. a-b, b-c, c-a -> trio

Since we are using an adjacency matrix we need an additional data structure to store degrees.

Time complexity: O(n^3). Space complexity: O(n^2)
"""
class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        degrees = defaultdict(int)
        graph = [[False for j in range(n+1)] for i in range(n+1)]
        
        for edge in edges:
            graph[edge[0]][edge[1]] = True
            graph[edge[1]][edge[0]] = True
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
        
        minDeg = float("inf")
        i1 = 0
        while i1 < n+1:
            i2 = i1+1
            while i2 < n+1:
                if graph[i1][i2]:
                    i3 = i2+1
                    while i3 < n+1:
                        if graph[i1][i3] and graph[i2][i3]:
                            minDeg = min(degrees[i1]+degrees[i2]+degrees[i3]-6, minDeg)
                        i3 += 1
                i2 += 1
            i1 += 1
        
        if minDeg == float("inf"):
            return -1
        return minDeg