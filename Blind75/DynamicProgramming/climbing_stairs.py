"""
https://leetcode.com/problems/climbing-stairs/

Fibonacci numbers: [1,2,1+2,2+1+2,...]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        prev,curr = 1,2
        for _ in range(2,n):
            prev,curr = curr,prev+curr
        return curr