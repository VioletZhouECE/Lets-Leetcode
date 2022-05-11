"""
https://leetcode.com/problems/combination-sum/
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.combinationSumHelper(candidates, target, [], result)
        return result
        
    def combinationSumHelper(self, candidates, target, temp, result):
        # base case
        if target == 0:
            result.append(temp.copy())
            return
        
        if target < 0:
            return
        
        for idx, num in enumerate(candidates):
            temp.append(num)
            self.combinationSumHelper(candidates[idx:], target-num, temp, result)
            temp.pop()