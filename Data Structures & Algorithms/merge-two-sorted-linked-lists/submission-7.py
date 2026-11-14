# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Goal is to do this in place by altering the linkages and not making new output
            * If we run out of one list, we append everything the other list has remaining
        '''
        l1 = list1
        l2 = list2  # roots of each

        if not l1:
            return l2
        if not l2:
            return l1   # if both are none this should still work --> returns none

        # We confirmed that l1 and l2 both exist
        dummy = ListNode()
        cur = dummy # traverses dummy for next

        # Todo logic
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # Final check to append the remaining list
        if l2:
            cur.next = l2
        if l1:
            cur.next = l1
            
        return dummy.next   # points to the start of the combined list