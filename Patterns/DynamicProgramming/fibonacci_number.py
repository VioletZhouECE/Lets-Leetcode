"""
https://leetcode.com/problems/fibonacci-number/
"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        first, second = 0, 1
        for i in range(2,n+1):
            first, second = second, first+second
        return second