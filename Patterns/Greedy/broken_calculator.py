"""
https://leetcode.com/problems/broken-calculator/

Key: If the number is even, maybe we should add 1*n to the number and then divide it by two. Is that going to make things better?
No, if you divide it by 2, it will be even closer to the value we are targeting. We should only add 1 to the number when we have to (aka when it becomes odd)
This allows us to make greedy choices: if even, /2, if odd, +1
"""
class Solution:
    #recursion
    def brokenCalc(self, startValue: int, target: int) -> int:
        if target <= startValue:
            return startValue-target
        if target%2 == 0:
            return 1+self.brokenCalc(startValue, int(target/2))
        return 1+self.brokenCalc(startValue, target+1)
    
    #iteration
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0
        while target > startValue:
            if target%2 == 0: target //= 2
            else: target += 1
            steps += 1
        return steps + (startValue-target)
    