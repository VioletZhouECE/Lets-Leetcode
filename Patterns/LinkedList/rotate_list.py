# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        #calculate the length
        length = 0
        curr = head
        last = head
        while curr != None:
            length += 1
            last = curr
            curr = curr.next
        
        #calculate the start index of the "rotation"
        index = length - k % length
        
        # special case: index = length: no rotation
        if index == length:
            return head
        
        curr = head
        prev = None
        currIndex = 0
        while currIndex != index:
            currIndex += 1
            prev = curr
            curr = curr.next
        
        prev.next = None
        last.next = head
        head = curr
        
        return head