# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        WE ARE IN PLACE REORDERING A LINKED LIST
        IT ALTERNATES FROM THE FIRST AND LAST NODE WTFFF?!?!?!?

        One strat:
        - go find the middle, reverse the second half of the list, and then add from each
        the last part is EASY MERGE LISTS OKAY

        WHEN FINDING THE MIDDLE WE DID SOME WEIRD TEK SO THAT THE SLOW NODE IS THE FINAL 
        NODE IN THE FIRST LIST

        how to reverse:   X -- Y --- Z
        1. make y point to x
        2. temp = z
        *** temp = x.next
        *** X point to prev (NULL)
        *** MOVE now temp curr = prev, temp  =curr

        '''

        # Find the middle of the lists
        dummy = head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the two halves
        head2 = slow.next
        slow.next = None

        # Reverse the second half starting from head2
        prev = None
        curr2 = head2
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        head1 = head
        head2 = prev # since the old head2 was in the middle
        while head1 and head2:
            t1 = head1.next
            t2 = head2.next
            
            head1.next = head2
            head2.next = t1
            
            head1 = t1
            head2 = t2
            
