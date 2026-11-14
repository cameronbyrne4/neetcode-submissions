# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        head = smallest one
        dummy = head

        when we run out of a list we just append the rest of the other one
        '''
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Initialize head
        head = ListNode()
        dummy = head

        # Iterative step:
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
                head.next = temp
                head = temp
            else:               # Case: L2 is smaller and needs to be added
                temp = list2
                list2 = list2.next
                head.next = temp
                head = temp

        # final add ons
        if list1:
            head.next = list1
        if list2:
            head.next = list2

        return dummy.next