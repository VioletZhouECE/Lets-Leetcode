"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

It is all about reusing the result from the previous computation:
The longest Substring Without Repeating Characters that starts at index i tells us a lot about the longest Substring Without Repeating Characters that starts at index i+1
    
"""
class Solution(object):
    """
    "Standard" solution (where the window is shrinked):
    If the window is valid - update; otherwise, move the left pointer until the window is valid again.
    (and we check its validity in the next iteration).
    """
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
                while s[left] != s[right]:
                    charSet.remove(s[left])
                    left += 1
                charSet.remove(s[left])
                left += 1
        
        return maxLength

    """
    How to slide the window "faster"?
    The index of the last occurrence of the repeating char + 1 = the starting index of the next window.
    Note: Our charSeen contain some old data as we did not update it when sliding the window, that's why we need to check left <= charSeen[s[right]].
    """
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSeen = {}
        left, right, maxLength = 0, 0, 0
        while right < len(s):
            if s[right] in charSeen and left <= charSeen[s[right]]:
                left = charSeen[s[right]] + 1
            maxLength = max(right-left+1, maxLength)
            charSeen[s[right]] = right
            right += 1
        
        return maxLength