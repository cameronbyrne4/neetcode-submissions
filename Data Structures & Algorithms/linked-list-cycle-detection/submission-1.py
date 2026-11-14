# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:   #len 0 or 1 are noit cyclic
            return False
        if head.next == head:
            return True

        slow = head
        fast = head.next

        while fast:
            if slow == fast:
                return True
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break

        
        # Fast hit the end!!!!
        return False
