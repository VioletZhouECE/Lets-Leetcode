"""
Greedily choose the number that contributes the most to fixing the diff
Time: O(nlogn)
"""
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # the diff that we need to fix
        diff = sum(nums1)-sum(nums2)
        
        # how much every number can contribute to fixing the diff
        diffList = []
        for num1 in nums1:
            # if nums1 is the larger array, we want the numbers in nums1 to be as large as possible so we can fix the diff by making it smaller
            if diff>0:
                diffList.append(num1-1)
            else:
                diffList.append(6-num1)
        for num2 in nums2:
            if diff>0:
                diffList.append(6-num2)
            else:
                diffList.append(num2-1)
                
        diffList.sort()
        diff = abs(diff)
        
        count = 0
        while diff > 0 and diffList:
            diff -= diffList.pop()
            count += 1
        
        if diff > 0:
            return -1
        return count