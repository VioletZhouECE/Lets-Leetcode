"""
https://leetcode.com/problems/subtree-of-another-tree/

DFS:
root: n nodes, subRoot: m nodes
Time complexity: O(m*n).
Space complexity: O(height(m)+height(n)). worst-case: O(m+n)
O(height(n)) comes from isSubtree, O(height(m)) comes from isSameTree
We need to store a "path" on stack (aka, the node and its sibling)

BFS runs faster for this question because the node we are searching for likely appear closer to the root than to the leaf
time.
Time complexity: O(m*n).
Space complexity: O(n+height(m)).  worst-case: O(m+n)

A very good comparision on DFS vs BFS on a tree btw:
https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, rootNode, subRootNode):
        if not (rootNode and subRootNode):
            return rootNode is subRootNode
        if rootNode.val == subRootNode.val:
            return self.isSameTree(rootNode.left, subRootNode.left) and self.isSameTree(rootNode.right, subRootNode.right)
        return False