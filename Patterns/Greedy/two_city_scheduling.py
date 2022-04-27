"""
https://leetcode.com/problems/two-city-scheduling/

1. Flatten the array and sort it, don't pick duplicate interviewers & don't exceed capacities for a city.
a counterexample:
[[10, 20], [11, 20000], [12, 30000], [12, 40000]]
for the 1st person, we should have picked 20 instead of 10.
The typical greedy algo won't work since we have the constraint that one person can't go to two places, 
so picking places one by one does not necessarily lead to the optimal solution. We need to consider A & B together (aka refund).

2. Send everyone to A, and send those with the smallest (B-A) to B (get the most refund)
Why does this work?
By maximizing the refund we get, we minimizes the overall cost
This is also greedy...tho a bit tricky
"""
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refunds = [cost[1]-cost[0] for cost in costs]
        minCosts = 0
        #send everyone to A
        for cost in costs:
            minCosts += cost[0]
            
        #sort refunds
        refunds = sorted(refunds)
        
        for i in range(len(costs)//2):
            minCosts += refunds[i]
        
        return minCosts
        