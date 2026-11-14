# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Checking if trees are the exact same?!
        # p and q instead of roots
        self.res = True
        def dfs(pp, qq):
            # if one doesn't exist
            if not pp and not qq:
                return None
            if pp and not qq:
                self.res = False
                return
            if qq and not pp:
                self.res = False
                return

            # both exist, value is different!
            if pp.val != qq.val:
                self.res = False   
            
            dfs(pp.left,qq.left)
            dfs(pp.right,qq.right)
             

        dfs(p,q)
        return self.res
