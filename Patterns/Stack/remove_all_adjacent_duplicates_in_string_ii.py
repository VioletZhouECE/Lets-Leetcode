"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

This is a good stack question.
recursive deletion -> stack.

Maintain a hashmap: {number: [length of each continuous sequence]}

Key:
We need to store the length so that we don't need to re-compute the length of the new continuous sequence after popping items.
Our hashmap entries act like a stack.
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counts = {}
    
        for char in s:
            if stack and char == stack[-1]:
                counts[char][-1] += 1
                stack.append(char)
                if counts[char][-1] == k:
                    for i in range(k):
                        stack.pop()
                    counts[char].pop()
            else:
                #start a new chunk
                if char not in counts:
                    counts[char] = []
                counts[char].append(1)
                stack.append(char)
        
        return "".join(stack)
                        
                        
        