"""
https://leetcode.com/problems/course-schedule-ii/

Runtime: O(n+m)
"""
class Solution:
    """
    DFS - slightly tedious cycle detection code
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #construct a graph
        prereqs = [[] for i in range(numCourses)]
        for prereq in prerequisites:
            prereqs[prereq[0]].append(prereq[1])
        
        #topological sort
        result = []
        #-1: not visited, 0: visiting, 1: visited
        visited = [-1 for n in range(numCourses)]
        
        for i in range(numCourses):
            if visited[i] == -1:
                hasCycle = self.dfs(i, prereqs, result, visited)
                if hasCycle == -1:
                    return []
        
        return result
    
    def dfs(self, i, prereqs, result, visited):
        visited[i] = 0
        
        for n in prereqs[i]:
            # check cycle
            if visited[n] == 0:
                return -1
            if visited[n] == -1:
                hasCycle = self.dfs(n, prereqs, result, visited)
                if hasCycle == -1:
                    return hasCycle
            
        visited[i] = 1
        result.append(i)

    """
    BFS - kahn's algorithm is always better :)
    """
    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegree = [0 for i in range(numCourses)]
        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            if prereq[1] not in graph:
                graph[prereq[1]] = []
            graph[prereq[1]].append(prereq[0])
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            if node in graph:
                for neighbour in graph[node]:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)
        
        for x in indegree:
            if x != 0:
                return []
        return result