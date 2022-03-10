# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i,j = l1,l2
        carry = 0
        head, prev = None, None
        
        while i or j or carry:
            curr1, curr2 = 0, 0
            if i: 
                curr1 = i.val
                i = i.next
            if j: 
                curr2 = j.val
                j = j.next
            carry, r = divmod(curr1 + curr2 + carry, 10)
            if not head:
                head = ListNode(r)
                prev = head
            else:
                prev.next = ListNode(r)
                prev = prev.next
        
        return head