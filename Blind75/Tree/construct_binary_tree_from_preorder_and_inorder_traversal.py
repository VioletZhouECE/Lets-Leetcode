"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

This is a divide and conquer problem, we construct one node at a time and do partitioning.
For every subtree,
Preorder traversal gives us root node, children nodes (left nodes + right nodes)
Inorder traversal tells us how to partition the children nodes to left nodes | right nodes

Takeaway: 
1. Divide and conquer algo is very commonly used in tree problems. Just focus on one node, its left children, its right children at a time.
2. When reasoning about the time and space complexity, actually write down the recurrence relation.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Time complexity: O(n^2). Space complexity: O(h)
    Best-case: T(n) = 2T(n/2) + O(n) -> T(n) = O(nlogn)
    Worst-case: T(n) = T(n-1) + O(n) -> T(n) = O(n^2)
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0], None, None)
        leftChildIndex = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:leftChildIndex+1], inorder[:leftChildIndex+1])
        root.right = self.buildTree(preorder[leftChildIndex+1:], inorder[leftChildIndex+1:])
        return root

    """
    Improvements: 
    1. Use a map to store the index to avoid having to search in the inorder array every time. 
    Note: leftChildIndex = map[preorder[prestart]]-instart.
    We need to -instart since map[preorder[prestart]] stores the position of preorder[prestart] in the ORIGINAL array.
    2. Pass the array by reference instead of making a copy and slicing it each time.

    Time complexity: O(n). Space complexity: O(n)
    Best-case: T(n) = 2T(n/2) + O(1) -> T(n) = O(n)
    Worst-case: T(n) = T(n-1) + O(1) -> T(n) = O(n)
    """
    def buildTreeImproved(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(prestart, preend, instart, inend, map):
            if prestart > preend:
                return None
            root = TreeNode(preorder[prestart], None, None)
            leftChildIndex = map[preorder[prestart]]-instart
            root.left = buildTreeHelper(prestart+1, prestart+leftChildIndex, instart, instart+leftChildIndex-1, map)
            root.right = buildTreeHelper(prestart+leftChildIndex+1, preend, instart+leftChildIndex+1, inend, map)
            return root
        
        map = {}
        for i, node in enumerate(inorder):
            map[node] = i
        return buildTreeHelper(0, len(preorder)-1, 0, len(inorder)-1, map)

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
        