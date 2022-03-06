"""
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

n=3 -> place P1 and D1 -> n=2 -> ...
3+2+1

Time complexity: O(n). Space complexity: O(n)
"""
class Solution:
    def countOrders(self, n: int) -> int:
        if n==1:
            return 1
        return (int(2*n*(2*n-1)/2) * self.countOrders(n-1)) % (pow(10,9)+7)