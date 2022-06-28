"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

This is not an optimization problem, there is only one solution.

Simulate finding a "spot" for each number: Place a number at the frequency slot if the slot is not occupied, otherwise decrease the frequency until you find an empty slot.
"""
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        
        totalDeletions = 0
        seen = set()
        for freq in sorted(freq.values()):
            currFreq = freq
            while currFreq in seen:
                currFreq -= 1
                totalDeletions += 1
            if currFreq: seen.add(currFreq)
        
        return totalDeletions