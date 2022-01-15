"""
https://leetcode.com/problems/longest-increasing-subsequence/

Time complexity: O(n^2). Space complexity: O(n)

The optimal solution is actually O(nlogn): 
https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengthArray = [1]*len(nums)
        maxLength = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    lengthArray[i] = max(lengthArray[i],lengthArray[j]+1)
            maxLength = max(maxLength, lengthArray[i])
                    
        return maxLength