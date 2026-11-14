# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        brute force: 
            put all them into one array and then sort it

        maybe:
            put all into a min heap and extract from there

        better:
            keep track of the k values in some data structure. HEAP
            -- track as a pair with the index of the k list so we know which list to remove from
            -- When you take out the minimum:
                -- add that to the result lsit
                -- add the head.next back into the heap

        Hint:
        - 
        '''
        # Edge case
        if len(lists) == 0:
            return None

        # Iterative step where we merge pairs of lists over and over until there's one left
        while len(lists) > 1:
            mergedlists = []
            # Select pairings
            for l in range(0, len(lists), 2):
                l1 = lists[l]
                # l2 is l+1 only if that's valid
                if l+1 < len(lists):
                    l2 = lists[l+1]
                else:
                    l2 = None
                mergedlists.append(self.mergelist(l1,l2))
            lists = mergedlists
        return lists[0]
                
    # Helper function for merging two lists and sorting
    # Merged in order until one of them doesn't exist. if the other does exist we can put it at the end
    def mergelist(self,l1,l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            # Append the minimum value to the dummy list, and shift that one down
            if l1.val < l2.val: # Add l1 to the dummy
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next                # ALMOST FORGOT THIS LINE
        
        # Now one of them has run out! Let's see if there are any stragglers
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next









