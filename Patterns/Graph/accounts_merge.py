"""
https://leetcode.com/problems/accounts-merge/

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

"""
Union find:
Ownership is a bijection between email and index: it tells us which emails are stored at each index
Path compression ensures that uf.find(index) is constant time (amortized over operations)

Runtime: O(n) where n is the total number of emails

Aside: Union find vs DFS
From CLRS: "When the edges of the graph are dynamic – changing over time – DFS is not a good choice since it cannot be applied progressively; we can compute the connected components faster by using union-find."
i.e. If you want to add a new edge, you will need to run DFS again on the entire graph to update the connected component, whereas with union find you can do this update in constant time.

"""
class UF:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        
    def union(self, child, parent):
        self.ids[self.getRoot(child)] = self.getRoot(parent)
        
    def getRoot(self, index):
        #base case: the root
        if index != self.ids[index]:
            # path compression - we builds a direct edge between every child node and the root
            self.ids[index] = self.getRoot(self.ids[index])
        return self.ids[index]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        ownership = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in ownership:
                    #union
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        #"collect" the emails: {root: [emails]}
        result = defaultdict(list)
        for email, index, in ownership.items():
            result[uf.getRoot(index)].append(email)
            
        return [[accounts[i][0]] + sorted(emails) for i, emails in result.items()]