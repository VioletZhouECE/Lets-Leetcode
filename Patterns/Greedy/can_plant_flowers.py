"""
https://leetcode.com/problems/can-place-flowers/

Greedily plant the flowers.
Smart: use flowerbed = [0] + flowerbed + [0] to avoid handling the first spot and the last spot separately lol.

Time complexity: O(n). Space complexity: O(1)
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return n == 0
        
        #Smart! This way we don't need to handle the first spot and the last spot separately
        flowerbed = [0] + flowerbed + [0]
        
        #greedily plant the flowers
        numOfFlowers = 0
        for i in range(1,len(flowerbed)-1):
            if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                flowerbed[i] = 1
                numOfFlowers += 1
        
        return numOfFlowers >= n