"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Steps:
1. pre-order traversal to pupolate a hashMap: {columnIndex: [(node, row)]}
2. sort by column index
3. sort each inner list by (row, node.val)

Time complexity: O(nlogn). Space complexity: O(n)

So yeah you can turn dict into a tuple and sort it by key by using sorted(dict.items())
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colNodes = defaultdict(list)
        self.preorderTraversal(root, colNodes, 0, 0)
        #sort by column index
        result = [entry[1] for entry in sorted(colNodes.items())]
        #sort each inner list by (row, node.val)
        for i in range(len(result)):
            result[i].sort(key=lambda tup: (tup[1], tup[0]))
            result[i] = [tup[0] for tup in result[i]]
        return result
        
    def preorderTraversal(self, node, colNodes, row, col):
        if not node:
            return
        colNodes[col].append((node.val, row))
        self.preorderTraversal(node.left, colNodes, row+1, col-1)
        self.preorderTraversal(node.right, colNodes, row+1, col+1)