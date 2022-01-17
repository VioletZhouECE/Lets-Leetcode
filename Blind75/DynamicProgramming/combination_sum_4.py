"""
https://leetcode.com/problems/combination-sum-iv/

Brutal force recursion: generate (almost) all the possible combinations that we can make with nums
combinationSum4(nums, target) = sum(combinationSum4(nums, target-i) for i in nums)
Duplicate computations: combinationSum4(nums, k) is computed many times for the same k
Time complexity: O(n^n) upper bound (when the tree has a height of n)

DP:
nums = [1,2,3], target = 4
dp=[1, 1, 1+1, 2+1+1, 4+2+1]
Time complexity: O(m*n). Space complexity: O(m) 
where n - len(nums), m - target

Note: the reason why we can iterate over the entire nums array and take any number is because we can reuse a number 
& order matters (different orders -> different combinations). Technically this question should be called Permutation Sum.

If negative numbers are allowed:
ex: [1,-1], target = 3
1+1+1
1+1+1+1-1
1+1+1+1+1-1-1
...
There could be infinite many combinations to make up a number
Limitions we can add: limit the number of times negative numbers can be used probably?
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combinations = [0]*(target+1)
        combinations[0] = 1
        
        for i in range(1, target+1):
            combinations[i] = sum(combinations[i-num] for num in nums if num<=i)
        
        return combinations[-1]