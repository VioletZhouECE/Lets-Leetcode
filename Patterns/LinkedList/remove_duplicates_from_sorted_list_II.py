"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr and curr.next:
            #delete the chain of duplicate nodes
            if curr.val == curr.next.val:
                end = curr.next
                while end and end.val == curr.val:
                    end = end.next
                if prev: 
                    prev.next = end
                else:
                    #we delete the head
                    head = end
                curr = end
            else:
                prev = curr
                curr = curr.next
        
        return head