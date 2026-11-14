# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        # move them to find midpoint
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # o o x o y
        # o o o x o o (y) 
        # Slow is the head of the list we have to reverse....
        prev = None
        second = slow.next            # offset for lists of even length
        slow.next = None # Split the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Now remake the output alternating from old half list and "prev" half list
        l = head
        while prev:
            t1, t2 = l.next, prev.next
            l.next = prev
            prev.next = t1
            l = t1
            prev = t2
            

