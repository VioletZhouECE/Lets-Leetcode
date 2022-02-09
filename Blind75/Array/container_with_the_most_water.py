"""
https://leetcode.com/problems/container-with-most-water/

Classic two pointer problem:

Violet's O(n) solution
Move left until curr.height > prev.height
Move right until curr.height >= left.height

Important note: Why do we never move the right pointer backward?
If we move it backward, the right line is going to decrease in height and determines the amount of water the container can hold: 
((height[right]*(right-left)) is going to be smaller than the previous solution we found at left-1 (height[right]*(right-left+1)) 
since the distance between left and right is smaller.

Thought process:
Think about how you can skip some checks and improve the brutal force solution:
1. Which starting index can we skip?
    curr.height <= prev.height
2. For each starting index, which ending index can we skip?
    Everything to the left of the right line which matches the height of the left line
3. Do we ever need to move the ending index backward?
    No. See the important note above.

A cleaner O(n) solution:
If height[left] < height[right]: move left
Otherwise: move right

Does essentially the same thing but I think this is more difficult to reason about ;)

"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = 0
        
        while left < right:
            #move left until curr.height > prev.height
            while left > 0 and height[left-1] > height[left] and left < right:
                left += 1
            #move right until curr.height >= left.height
            while height[right] < height[left] and left < right:
                maxWater = max(maxWater, height[right]*(right-left))
                right -= 1
            maxWater = max(maxWater, height[left]*(right-left))
            #don't forget this!
            left += 1
            
        return maxWater