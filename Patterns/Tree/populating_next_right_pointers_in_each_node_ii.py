"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    """
    Big brain pointer solution: O(n) time O(1) space
    We can actually link children together at the parent's level because we have the next pointer (so smart!)
    Reference: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37828/O(1)-space-O(n)-complexity-Iterative-Solution
    """
    def connect(self, root: 'Node') -> 'Node':
        head = root
        #when the new head is none (all the nodes at the previous level are leaves), we stop
        while head:
            #prev-previous node at the next level
            #head-leading node at the next level
            #curr-current node at the current level
            prev = None
            curr = head
            head = None
            #iterate through the current level
            while curr:
                #prev->left
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        head = curr.left
                    prev = curr.left
                #left->right
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        head = curr.right
                    prev = curr.right
                curr = curr.next
        return root
    """
    Small brain level-order traversal: O(n) time O(n) space
    """
    def connect2(self, root: 'Node') -> 'Node':
        if not root: return root
        
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            prev = None
            for i in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if prev:
                    prev.next = node
                prev = node
        
        return root