"""
https://leetcode.com/problems/alien-dictionary/

4 scenarios when constructing the graph:
wa wrf: a->r
wrf wr: impossible (NOTE: we need to handle this as a special case)
wr wrf: no information (do nothing)
wa wa: no information (do nothing)

Remember to include chars that are not in the graph:
- How to get unvisited chars:
    set("".join(words)) - all nodes in the graph (state.keys())
     
Time complexity: O(k) where k is the number of characters. Space complexity: O(k)
"""
class Solution:
    """
    DFS
    """
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        allChars = set("".join(words))
       
        for i in range(1,len(words)):
            prevWord = words[i-1]
            currWord = words[i] 
            #find the first char that differs
            i = 0
            
            while i<len(prevWord) and i<len(currWord):
                if prevWord[i] != currWord[i]:
                    break
                i += 1
            
            if i<len(prevWord) and i<len(currWord):
                if prevWord[i] not in graph:
                    graph[prevWord[i]] = []
                graph[prevWord[i]].append(currWord[i])
            elif i==len(currWord) and i<len(prevWord):
                return ""
            
        # 1: visiting, 2: visited
        state = {}   
        result = []
        for v in graph.keys():
            if v not in state:
                if not self.dfs(v, graph, state, result):
                    return ""
    
        unvisitedChars = list(allChars.difference(set(state.keys())))
        result.extend(unvisitedChars)
        result.reverse()
        
        return "".join(result)
            
    def dfs(self, node, graph, state, result):
        state[node] = 1
        if node in graph:
            for neighbour in graph[node]:
                if neighbour not in state:
                    if not self.dfs(neighbour, graph, state, result):
                        return False
                if state[neighbour] == 1:
                    return False
        result.append(node)
        state[node] = 2
        return True

    """
    BFS - kahn's algorithm
    """
    def alienOrder2(self, words: List[str]) -> str:
        graph = {}
        allChars = set("".join(words))
        indegrees = {}
       
        for i in range(1,len(words)):
            prevWord = words[i-1]
            currWord = words[i] 
            #find the first char that differs
            i = 0
            
            while i<len(prevWord) and i<len(currWord):
                if prevWord[i] != currWord[i]:
                    break
                i += 1
            
            if i<len(prevWord) and i<len(currWord):
                if prevWord[i] not in graph:
                    graph[prevWord[i]] = []
                    indegrees[prevWord[i]] = 0
                graph[prevWord[i]].append(currWord[i])
                if currWord[i] not in indegrees:
                    indegrees[currWord[i]] = 0
                    graph[currWord[i]] = []
                indegrees[currWord[i]] += 1
            elif i==len(currWord) and i<len(prevWord):
                return ""
        
        result = []
        self.bfs(graph, indegrees, result)
        #cycle detection
        if len(result) != len(graph.keys()):
            return ""
        unvisitedChars = list(allChars.difference(set(graph.keys())))
        result.extend(unvisitedChars)
        
        return "".join(result)
        
    def bfs(self, graph, indegrees, result):
        queue = deque()
        
        for i in indegrees.keys():
            if indegrees[i] == 0:
                queue.append(i)
            
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbour in graph[node]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)