"""
Graph (DFS/BFS):
1. Create a graph where each node reprensents an email.
2. Use an additional set to keep track of the owner of these emails.
3. Traverse the graph (DFS/BFS) ro read each connected component.

DFS:
Be careful when you use defaultdict(set)! 
When you access a non-existent node in the for loop - for email, neighbours in graph.items(),
it will atomatically add the node into the dictionary and python will throw an error as you change the size of the dictionary while iterating it.
So make sure that you have all the nodes as a dictionary key

BFS:
Basically another way to traverse the connected component lol

"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #we use set here since there could be duplicate emails
        graph = defaultdict(set)
        emailToName = defaultdict(str)
        
        for account in accounts:
            firstName = account[0]
            firstEmail = account[1]
            #undirected graph
            for email in account[1:]:
                graph[firstEmail].add(email)
                #technically, we don't need to build this edge, 
                #but this adds the email node into the graph and make the dfs easier
                graph[email].add(firstEmail)
                emailToName[email] = firstName
        
        result = []
        seen = set()
        for email, neighbours in graph.items():
            if email in graph and email not in seen:
                emails = []
                self.dfs(email, graph, seen, emails)
                result.append([emailToName[email]] + sorted(emails))
        
        return result
                
    def dfs(self, node, graph, seen, components):
        if node in seen:
            return
        components.append(node)
        seen.add(node)
        for neighbour in graph[node]:
            if neighbour in graph and neighbour not in seen:
                self.dfs(neighbour, graph, seen, components)