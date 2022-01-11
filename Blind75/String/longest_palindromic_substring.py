"""
https://leetcode.com/problems/longest-palindromic-substring/

The wrong reccurence relation:
if s[j] == s[j]:
    LPS(i,j,s) = LPS(i+1,j-1,s) + 2
else:
    LPS(i,j,s) = max(LPS(i+1,j,s), LPS(i,j-1,s))
    
Why is it wrong?
This will skip some characters in the middle and return a subsequence instead of a substring. You are essentially solving the problem - Longest Palindromic Subsequence lmao.
Note: 

Key:
We should expand the palindrom starting from the middle.
Why is it faster than starting from both ends (the brutal force solution):
    Because expanding from the middle allows us to stop earlier.
    i.e. 'baba' - if we already know ab is not a palindrom, we don't need to expand and check 'baba'.
    
This is DP (though it is not very obvious) - reuse the result of the previous computation:
    'ab' is not a palindrom -> 'baba' is also not a palindrom. 
    'aa' is a palindrom -> 'baab' is also a palindrom.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestStr = ''
        for i in range(len(s)):
            oddStr = self.getPalindromeLength(s,i,i)
            evenStr = self.getPalindromeLength(s,i,i+1)
            if len(oddStr) > len(evenStr) and len(oddStr) > len(longestStr):
                longestStr = oddStr
            elif len(evenStr) > len(longestStr):
                longestStr = evenStr
        return longestStr
        
    def getPalindromeLength(self, s, left, right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]