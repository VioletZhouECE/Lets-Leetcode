"""
https://leetcode.com/problems/valid-parentheses/
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matched = {')': '(', '}': '{',']': '['}
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            else:
                if not stack:
                    return False
                if matched[char] != stack[-1]:
                    return False
                stack.pop()
                
        return len(stack) == 0