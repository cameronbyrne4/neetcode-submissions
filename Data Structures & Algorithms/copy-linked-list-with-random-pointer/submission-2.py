"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Problem: We can't just create things right away because the random pointer will point to nothing
        '''

        # This maps the old numbers to their newly made retarded ass nodes
        copies = defaultdict()
        copies[None] = None
        # iterate thru the original list and add shit to the hash
        curr = head
        while curr:
            copy = Node(curr.val)
            copies[curr] = copy
            curr = curr.next

        # Now iterate again and assign the next and random
        curr = head
        while curr:
            copy = copies[curr]     # So far only has val
            copy.next = copies[curr.next]
            copy.random = copies[curr.random]           # This case failed for when curr was none, at the very end
            curr = curr.next
        return copies[head]