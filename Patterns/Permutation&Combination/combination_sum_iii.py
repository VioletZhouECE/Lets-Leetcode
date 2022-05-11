"""
https://leetcode.com/problems/combination-sum-iii/
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.combinationSum3Helper(k, n, 1, [], result)
        return result
    
    def combinationSum3Helper(self, k, n, start, temp, result):
        if n == 0 and k == 0:
            result.append(temp.copy())
        if n < 0 or k == 0:
            return
        for x in range(start,10):
            temp.append(x)
            self.combinationSum3Helper(k-1, n-x, x+1, temp, result)
            temp.pop()