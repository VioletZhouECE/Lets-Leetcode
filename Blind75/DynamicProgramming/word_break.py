"""
https://leetcode.com/problems/word-break/

Time complexity: O(n^2). 
Space complexity: O(n+m) where n is the length of the string and m is the size of the wordDict.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canBreak = [False]*len(s)
        wordSet = set(wordDict)
        
        for i in range(len(s)):
            #i-j goes from i to 0, so j goes from 0 to i
            for j in range(i+1):
                if s[i-j:i+1] in wordSet:
                    if i-j == 0 or canBreak[i-j-1]:
                        canBreak[i] = True
                        break
                        
        return canBreak[-1]

    """
    I don't think this is as readable tbh
    """
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        canBreak = [False]*(len(s)+1)
        canBreak[0] = True
        wordSet = set(wordDict)
        
        for i in range(1,len(s)+1):
            #note that index i in canBreak maps to i-1 in s
            canBreak[i] = any(canBreak[j] and s[j:i] in wordSet for j in range(i))
                
        return canBreak[-1]