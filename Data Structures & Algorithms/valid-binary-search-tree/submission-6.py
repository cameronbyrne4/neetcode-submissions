# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # i can pass in the current node value?
        # or set a l and r bound
        # If go left --> set a new right bound
        # if go right --> set a new low bound
        # both start as null tho
        self.res = True
        def dfs(x, low, hi):
            if not x:
                return None
            if x.val <= low or x.val >= hi:
                self.res = False
            

            dfs(x.left, low, x.val)
            dfs(x.right, x.val, hi)
        dfs(root, -9999, 9999)
        return self.res