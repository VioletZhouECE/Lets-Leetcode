"""
https://leetcode.com/problems/custom-sort-string/

Throw a hashMap at the problem moment :)
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(list(s))
        result = []
        for char in order:
            if char in counts:
                result += [char] * counts[char]
                counts[char] = 0
            
        #append characters that are not present in order
        for char, num in counts.items():
            result += [char] * num
            counts[char] = 0
        
        return ''.join(result)