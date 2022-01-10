"""
https://leetcode.com/problems/longest-repeating-character-replacement/

Reference: a very elegant solution where we never shrink the window:
https://leetcode.com/problems/longest-repeating-character-replacement/discuss/700321/Python-Simple-O(N)-solution-with-explanation

The idea is that we always maintain a valid window:
valid - expand the window (right += 1); invalid - slide the window (left += 1, right += 1)

Keys:
1. Which character to replace? We always replace with the most frequent character (and we need to update the frequency map in every step - everytime we check the validity of the window).
2. Since we are looking for the longest substring, we don't need to shrink the window (as shrinking the window makes the substring shorter).
    Sometimes we do need to shrink the window: i.e. 73. Minimum Window Substring.

This is better than the solution where we shrink the window in terms of code simplicity and runtime.
"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLength, maxFreq, left, right = 0, 0, 0, 0
        mostFreqLetter = '0'
        frequencyMap = {'0': 0}
        
        while right < len(s):
            frequencyMap[s[right]] = frequencyMap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, frequencyMap[s[right]])
            #the window is invalid, move left
            if right-left+1-maxFreq > k:
                frequencyMap[s[left]] -= 1
                left += 1
            else:
            #the window is valid, update maxLength
                maxLength = max(maxLength, right-left+1)
            right += 1
            
        return maxLength
                    