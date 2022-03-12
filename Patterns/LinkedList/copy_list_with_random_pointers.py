"""
https://leetcode.com/problems/copy-list-with-random-pointer/

How we handle cycles: 
1 <-> 2: As we store the node in newNodes before doing a dfs on next, so 2 can find the 1 that has been created in newNodes and directly link to it.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newNodes = {}
        return self.createNode(head, newNodes)
    
    def createNode(self, node, newNodes):
        if not node:
            return node
        
        if node in newNodes:
            return newNodes[node]
        
        newNode = Node(node.val)
        newNodes[node] = newNode
        newNode.next = self.createNode(node.next, newNodes)
        newNode.random = self.createNode(node.random, newNodes)
        
        return newNode