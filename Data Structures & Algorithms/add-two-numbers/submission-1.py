# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        -- input: 2 nums stored with backwards digits in a linked list
        -- outout: linked list with the sum (also backwards order)

        strat:
            we gotta go digit by digit
            add l1 digit + l2 digit + carry value (starts as 0, is any excess over 9)
            if there is excess at the end we gotta append it

            vals are 0 if the list is done
        '''
        carry = 0
        dummy = ListNode()
        head = dummy
        while l1 or l2:
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            curSum = x + y + carry
            carry = 0

            # Readjust for overflow
            if curSum > 9:
                curSum -= 10            
                carry = 1

            dummy.next = ListNode(curSum)
            dummy = dummy.next
            # Move to next digits
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Final digit
        if carry:
            dummy.next = ListNode(carry)

        return head.next



