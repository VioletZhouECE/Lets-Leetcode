"""
https://leetcode.com/problems/candy/

This is a tricky problem
https://www.youtube.com/watch?v=h6_lIwZYHQw

Key: it's too difficult to consider the left neighbour and the right neighbour at the same time, so we break the problem down into two subproblems and merge the solutions
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        numOfChildren = len(ratings)
        leftToRight = [1 for _ in range(numOfChildren)]
        rightToLeft = [1 for _ in range(numOfChildren)]
        
        for i in range(1,len(ratings)):
            if ratings[i-1] < ratings[i]:
                leftToRight[i] = leftToRight[i-1]+1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                rightToLeft[i] = rightToLeft[i+1]+1
        
        numCandies = 0
        for i in range(len(ratings)):
            numCandies += max(leftToRight[i], rightToLeft[i])
            
        return numCandies