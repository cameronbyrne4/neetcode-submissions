# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        I forgot how to traverse trees and how the pre/post/in-order works for what cases

        Base cases:
            false if just ONE is null or both exist and not equal
        '''
        if not p and not q:
            return True
        elif (not p and q) or (not q and p):
            return False
        elif (p and q) and (p.val != q.val):
            return False
        else:
            # Both exist and have same values, need to recurse on children
            return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
            