"""
https://leetcode.com/problems/permutations-ii/
"""
class Solution:
    """
    What numbers can we insert at this index?
    The use of the dictionary takes care of handling duplicates
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        numDict = Counter(nums)
        self.permuteUniqueHelper(numDict, [], result)
        return result
        
    def permuteUniqueHelper(self, nums, temp, result):
        unvisited = True
        for k in nums.keys():
            if nums[k] > 0:
                unvisited = False
                temp.append(k)
                nums[k] -= 1
                self.permuteUniqueHelper(nums, temp, result)
                temp.pop()
                nums[k] += 1
        if unvisited:
            result.append(temp.copy())

    """
    At which index can we insert this number?
    Note: we need to handle duplicates
    """
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            newRes = []
            for r in res:
                for i in range(len(r)+1):
                    #insert n at index i
                    newRes.append(r[:i]+[n]+r[i:])
                    #handle duplicates
                    if i<len(r) and r[i] == n: break
            res = newRes
        return res