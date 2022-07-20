# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
"""
https://leetcode.com/problems/find-the-celebrity/
The key is to ask as few questions as possible

A, B, C
A knows B: A is not the celebrity, B might be the celebrity
C knows B: C is not the celebrity, B is the celebrity

A, B, C, D
A doesn't know B: B is not the celebrity
A knows C: A is not the celebrity, C might be the celebrity

Finding: asking a question eliminates one candidate, the one left is the candidate for celebrity

Now we need to verify that everyone knows the celebrity and that the celebrity doesn't know anyone except themselves
"""
class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(1,n):
            if knows(celebrity, i):
                celebrity = i
        
        # verify that everyone knows the celebrity
        for i in range(n):
            if not knows(i, celebrity):
                return -1
            
        # verify that the celebrity doesn't know anyone except themselves
        for i in range(n):
            if i != celebrity and knows(celebrity, i):
                return -1
            
        return celebrity