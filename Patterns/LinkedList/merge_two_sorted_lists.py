"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    In-place:
    We try to insert list2 into list1 (so we return list1).
    3 things to note here:
        1. we insert list2 in front of p1, so we need prev.
        2. dummy head (again).
        3. it would be helpful to draw the linked list and think about how you would change the linkage.
    """
    def mergeTwoListsInPlace(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        dummy = prev = ListNode(0, None)
        dummy.next = list1
        
        while list1 and list2:
            if list1.val < list2.val:
                #update prev and forward list1
                prev = list1
                list1 = list1.next
            else:
                #copy list2.next
                temp2 = list2.next
                #insert list2 before list1
                list2.next = list1
                prev.next = list2
                #update prev and forward list2
                prev = list2
                list2 = temp2
        
        if not list1: prev.next = list2
            
        return dummy.next

    """
    Create a new list:
    2 things to note here:
        1. dummy head: we don't need to have a if statement for setting the head
        2. while list1 and list2 is better than while list1 or list2: for the latter, we need to check if not list1, if not list2, etc.
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        dummy = prev = ListNode(0, None)
        dummy.next = list1
        
        while list1 and list2:
            if list1.val < list2.val:
                prev = list1
                list1 = list1.next
            else:
                temp2 = list2.next
                list2.next = list1
                prev.next = list2
                prev = list2
                list2 = temp2
        
        if not list1: prev.next = list2
            
        return dummy.next
                