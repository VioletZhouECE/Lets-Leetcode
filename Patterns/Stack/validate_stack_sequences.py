"""
https://leetcode.com/problems/validate-stack-sequences/

This is a simulation problem
Since there is no distinct value, we don't need to make a decision about whether we should pop the item or not. If stack[-1] == popped[i], we pop it.

Time complexity: O(n). Space complexity: O(n)
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for p in pushed:
            stack.append(p)
            #try popping as many items as possible
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return not stack