"""
https://leetcode.com/problems/valid-anagram/

Determine if something is a anagram:
 1. Sort
 2. Count the number of characters:
    Note that in this case we can use an array of size 26 to store the count since we only have lowercase English letters.
    
Time complexity: O(n). Space complexity: O(1) - charCount1 and charCount2 have a fixed size
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        charCount1, charCount2 = [0] * 26, [0] * 26
        for char in s:
            charCount1[ord(char)-ord('a')] += 1
        for char in t:
            charCount2[ord(char)-ord('a')] += 1
        return charCount1 == charCount2