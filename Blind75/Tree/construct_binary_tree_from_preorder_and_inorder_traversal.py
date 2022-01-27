"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

This is a divide and conquer problem, we construct one node at a time and do partitioning.
For every subtree,
Preorder traversal gives us root node, children nodes (left nodes + right nodes)
Inorder traversal tells us how to partition the children nodes to left nodes | right nodes

Time complexity: O(n). Space complexity: O(h) - same as tree traversal

Takeaway: divide and conquer algo is very commonly used in tree problems. Just focus on one node, its left children, its right children at a time.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeHelper(preorder, inorder)
        
    def buildTreeHelper(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0], None, None)
        leftChildIndex = inorder.index(preorder[0])
        root.left = self.buildTreeHelper(preorder[1:leftChildIndex+1], inorder[:leftChildIndex+1])
        root.right = self.buildTreeHelper(preorder[leftChildIndex+1:], inorder[leftChildIndex+1:])
        return root
        