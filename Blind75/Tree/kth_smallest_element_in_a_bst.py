"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Recursion: 
Code is a bit ugly as we need to use a global variable numOfNodes to keep track of the number of nodes visited. Every recursive call returns numOfNodes traversed and the kth value (None if not found).
Since Python does not have pass by reference we need to pass and return numOfNodes lmao.
 
Time complexity: O(n). Space complexity: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        numOfNodes, val = self.inorderTraversal(root, 0, k)
        return val
    
    def inorderTraversal(self, root, numOfNodes, k):
        if root is None:
            return numOfNodes, None
        numOfNodes, kth = self.inorderTraversal(root.left, numOfNodes, k)
        if kth is not None: return numOfNodes, kth
        numOfNodes += 1
        if numOfNodes == k: return numOfNodes, root.val
        return self.inorderTraversal(root.right, numOfNodes, k)