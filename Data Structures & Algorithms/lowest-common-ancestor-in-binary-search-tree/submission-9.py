# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Return the LAST node where p and q are in the child trees anywhere
            # meaning update it over time
        #okay so i didn't realize it was a BST, meaning its in value order.
        # Result must be between p and q
        ###
        
         # moves down, closer to p and q
        if not root:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Otherwise, this is the split point
        return root


        