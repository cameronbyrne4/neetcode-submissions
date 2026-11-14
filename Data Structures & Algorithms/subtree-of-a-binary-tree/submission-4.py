# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Looking for subtrees
        # Only starts if some val in root true == subroot
        self.res = False
        
        def dfs_compare(pp, qq):
            # if one doesn't exist
            if not pp and not qq:
                return None
            if pp and not qq:
                self.res = False
                return # MUST HAVE THESE so the null cases doesn't still try to compare vals
            if qq and not pp:
                self.res = False
                return

            # both exist, value is different!
            if pp.val != qq.val:
                self.res = False   
            
            dfs_compare(pp.left,qq.left)
            dfs_compare(pp.right,qq.right)

        def dfs(x, v): # val is the subRoot.val
            # base case, nothing there
            if not x:
                return None
            
            # second base case, comparing to subroot
            if x.val == v:
                self.res = True
                dfs_compare(x,subRoot) # Updates self-res to false if they arent the same
                if self.res == True:
                    return self.res

            dfs(x.left,v)
            dfs(x.right,v)
        dfs(root,subRoot.val)
        return self.res