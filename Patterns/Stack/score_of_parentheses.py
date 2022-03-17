"""
https://leetcode.com/problems/score-of-parentheses/

Example:
(()(()))
1*2+1*2*2

Recursion: Yeah I guess we can try doing that... but it is not easy to extract the sublists since we are dealing with a string, not a data structure like in Nested List Weighted Sum.
Iteration: Yes! This is much cleaner. We just update the depth/level as you go through the list. ezpz

Time complexiy: O(n). Space complexity: O(1)
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        level = 0
        score = 0
        isOpenParen = True
        
        for char in s:
            if char == "(":
                if isOpenParen:
                    level += 1
                isOpenParen = True
            else:
                if isOpenParen:
                    score += pow(2,level-1)
                else:
                    level -= 1
                isOpenParen = False
            
        return score