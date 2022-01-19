"""
https://leetcode.com/problems/top-k-frequent-elements/

1. hashMap + sort - Time: O(nlogn). Space: O(n)
2. hashMap + heap - Time: O(nlogk). Space: O(n)
3. hashMap + quickSelect - Time: O(n). Space: O(n)
4. bucket sort (best) - Time: O(n). Space: O(n)
   integers + the range of the numbers we are sorting is [1,n] -> bucket sort!
   Space
"""
import heapq

class Solution:
    #O(n)
    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range((len(nums)+1))]
        counts = dict(collections.Counter(nums))
        for num, count in counts.items(): 
            bucket[count].append(num)
        result = []
        for nums in bucket[::-1]:
            if len(result) == k: 
                break
            result.extend(nums)
        return result

    #O(nlogk)
    def topKFrequentMinHeap(self, nums: List[int], k: int) -> List[int]:
        counts = dict(collections.Counter(nums))
        
        heap = []
        for num, count in counts.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))
        
        return [num for count, num in heap]