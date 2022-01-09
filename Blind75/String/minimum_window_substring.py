"""
https://leetcode.com/problems/minimum-window-substring/

Idea is similar to 3. Longest Substring Without Repeating Characters

Why does this work?
We are trying to find the min window substring that starts at each index
Suppose that we've found the min window substring starting at index 0
    1. If removing char at index 1 does not invalidate the window, min window substring starting at index 1  -> in window substring starting at index 0 - 1.
    2. If removing char at index 1 invalidates the window, then we need to move the right pointer until we find a char that validates the window again - that's the min window substring starting at index 1.
    
Essence of sliding window: 
    The window we've found starting at index 0 (and other info we computed, in this case the charMap) helps us find the window starting at index 1. 
    We never need to move the pointer backward as we have effectively compute useful information (charMap) as we traverse the string and keep it updated.
    It's about reusing information from previous computation.
    The window maintains a valid window substring, and the charMap stores useful information to identify if the current char will validate/invalidate the window.

Thoughts: we can only apply sliding window to substring/continueous subsequence because otherwise we don't have a window and the nice "chop from left, add from right" pattern.
    
Time complexity: O(n) as we never move the pointer backward
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        targetSet = set(t)
        targetMap = {}
        for char in t:
            targetMap[char] = targetMap.get(char, 0) + 1
            
        left = 0
        right = 0
        charMap = {}
        #charCount keeps track of how many valid chars we found - chars that contributes to forming t
        charCount = 0
        minSize = float("inf")
        minWindowSubstr = ""
        while right < len(s):
            if s[right] in targetSet:
                charMap[s[right]] = charMap.get(s[right], 0) + 1
                if charMap[s[right]] <= targetMap[s[right]]:
                    charCount += 1
                #check if we've found a window substring
                if charCount == len(t):
                    while left < right:
                        if s[left] in targetSet:
                            charMap[s[left]] = charMap[s[left]] - 1
                            # break when we found a char that invalidates the current window
                            if charMap[s[left]] < targetMap[s[left]]:
                                break
                        left += 1
                    #minimum window substring
                    if right-left+1 < minSize:
                        minWindowSubstr = s[left:right+1]
                        minSize = right-left+1
                    #left points at the starting point of the next window
                    left += 1
                    right += 1
                    charCount -= 1
                    continue
            right += 1
            
        return minWindowSubstr
        