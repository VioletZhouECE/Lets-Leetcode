"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

This is a divide and conquer problem, we construct one node at a time and do partitioning.
For every subtree,
Preorder traversal gives us root node, children nodes (left nodes + right nodes)
Inorder traversal tells us how to partition the children nodes to left nodes | right nodes

Time complexity: O(n^2). Space complexity: O(h) - same as tree traversal
Best-case: T(n) = 2T(n/2) + O(n) -> T(n) = O(nlogn)
Worst-case: T(n) = 2T(n-1) + O(n) -> T(n) = O(n^2)

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
        if not preorder:
            return None
        root = TreeNode(preorder[0], None, None)
        leftChildIndex = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:leftChildIndex+1], inorder[:leftChildIndex+1])
        root.right = self.buildTree(preorder[leftChildIndex+1:], inorder[leftChildIndex+1:])
        return root

"""
A similar question: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root = TreeNode(postorder[-1], None, None)
        numOfLeftChild = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:numOfLeftChild], postorder[:numOfLeftChild])
        root.right = self.buildTree(inorder[numOfLeftChild+1:], postorder[numOfLeftChild:len(postorder)-1])
        return root
        