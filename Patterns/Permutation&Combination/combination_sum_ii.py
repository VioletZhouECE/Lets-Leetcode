"""
This one is tricky ...
https://leetcode.com/problems/combination-sum-ii/

https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments

How to deal with duplicates in candidates?
Always take the first number of the chunk of repeated numbers and ignore the later ones.
"""
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()                      
        result = []
        self.combinationSum2Helper(candidates, target, 0, [], result)
        return result

    def combinationSum2Helper(self, nums, target, start, temp, result):
        if target == 0:
            result.append(temp.copy())
            return
        if target<0:
            return
        for i in range(start, len(nums)):
            #only take the first number of the chunk of repeated numbers
            if i > start and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.combinationSum2Helper(nums, target - nums[i], i + 1, temp, 
                               result)
            temp.pop()