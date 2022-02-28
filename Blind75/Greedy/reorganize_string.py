"""
https://leetcode.com/problems/reorganize-string/

Greedily choose the most frequent char
Keep a priority queue: (frequency, letter)

Why does this work?
Intuitively, it is more difficult to "split" the most frequent chars because there are too many of them, so we need to do this as early as possible when there are many other available chars. If we do this last, we won't have enought chars to "split" the most frequent chars.
So this is a choice that is the best so far and leads to better future outcomes.

Key:
The key is to not add the char to the queue in the current iteration, but in the next iteration. This ensures that we won't be having adjacent chars (no need to check for this explicitly).

Time complexity: O(nlogn). Space complexity: O(n)

Side note: This can be solved in O(n): the only thing we care about is the order of the most frequent letters, the rest does not matter. I personally think the O(n) solution is less intuitive though.
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        newString = []
        frequency = [] #a max pq
        
        #initialize the priority queue
        for char, freq in Counter(list(s)).items():
            heapq.heappush(frequency, (-freq, char))
            
        prevFreq, prevChar = 0, ''
        
        while frequency:
            freq, char = heapq.heappop(frequency)
            newString.append(char)
            if prevFreq < 0:
                heapq.heappush(frequency, (prevFreq, prevChar))
            freq += 1
            prevFreq, prevChar = freq, char
            
        if len(newString) != len(s): 
            return ""
        return "".join(newString)
            