# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        1. one pass to find length
        2. 2nd pass to remove 
        3. return head!
        '''
        # 1: find number of nodes
        p1 = head
        numNodes = 0
        while p1:
            numNodes += 1
            p1 = p1.next

        # Calculate which one from front we remove
        n = numNodes -n+1
            # n is now "remove the nth node"
        if n == 1:
            return head.next

        #2: remove it
        p2 = head
        i = 1

        while p2.next:
            i += 1
            if i == n:
                # Work to remove p2.next
                p2.next = p2.next.next
                break
            p2 = p2.next

        return head