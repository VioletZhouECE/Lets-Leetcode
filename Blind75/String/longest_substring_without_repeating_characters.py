"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

It is all about reusing the result from the previous computation:
The longest Substring Without Repeating Characters that starts at index i tells us a lot about the longest Substring Without Repeating Characters that starts at index i+1
    
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        left, right, maxLength = 0, 0, 0
        while right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right-left+1)
                right += 1
            else:
                #move the left pointer until we encounter the char that is the same as s[right] - after removing that char, we might be able to find a longer substring starting at index left+1.
                while left < right:
                    charSet.remove(s[left])
                    if s[left] == s[right]:
                        break
                    left += 1
                #s[left] == s[right]
                left += 1
        
        return maxLength