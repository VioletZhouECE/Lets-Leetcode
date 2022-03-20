"""
https://leetcode.com/problems/maximum-frequency-stack/

I am blown away by this O(1) solution :O
2 data structures:
helper - frequency map (to quickly find out where to insert the number) & 
main ds - a map of stacks (to quickly find out what is the next most frequent number)

Key:
If the current stack is empty, we know that the next "frequency" must be self.maxFreq -= 1! The fact that the keys of the map are contiguous integers is helpful.
We can use frequency as the key of mapping and quickly look up the key == self.maxFreq.
Let's let the "frequency" be contiguous :)

Time complexity: O(1). Space complexity: O(n)

Observation: If we change this question a bit,
ex1. we need to delete the most frequent number 
ex2. we need to increment the frequency by x
then this solution will not work anymore because it relies on the pattern of push(add 1) & pop(remove 1). 
We need to resort to our old friend pq.
"""
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.map = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.map[self.freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freq[val])

    def pop(self) -> int:
        popped = self.map[self.maxFreq].pop()
        self.freq[popped] -= 1
        #empty list
        if not self.map[self.maxFreq]:
            del self.map[self.maxFreq]
            self.maxFreq -= 1
        return popped
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()