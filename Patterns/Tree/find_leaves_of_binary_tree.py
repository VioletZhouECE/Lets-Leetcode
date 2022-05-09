"""
https://leetcode.com/problems/find-leaves-of-binary-tree/

A lot of tree problems have a recursive nature
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [[] for i in range(100)]
        self.placeLeaves(root, result)
        res = []
        for x in result:
            if len(x)>0:
                res.append(x)
        return res
        
    def placeLeaves(self, node, result):
        if not node:
            return -1
        leftLevel = self.placeLeaves(node.left, result)
        rightLevel = self.placeLeaves(node.right, result)
        result[max(leftLevel, rightLevel)+1].append(node.val)
        return max(leftLevel, rightLevel)+1