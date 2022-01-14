"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Pattern:
update map/set/the helper data structure,
fix the window if it is not valid (move the left pointer until the window is valid again).
update maxLength
"""
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLength = 0
        charMap = {}
        left = 0
        right = 0
        
        while right < len(s):
            charMap[s[right]] = charMap.get(s[right], 0) + 1
            #'fix' the window by moving the left pointer
            while len(charMap) > k:
                    charMap[s[left]] = charMap[s[left]] - 1
                    if charMap[s[left]] == 0:
                        del charMap[s[left]]    
                    left += 1
            maxLength = max(right-left+1, maxLength)
            right += 1
                    
        return maxLength