# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        literally at every node that has children, switch them around
        '''
        dummy = root

        def dfs(r):
            # return if no r
            # switch r's kids
            # do it to them too
            if (not r) or (r.left is None and r.right is None):
                return
            temp = r.right
            r.right = r.left
            r.left = temp

            dfs(r.left)
            dfs(r.right)
        dfs(root)
                
        return dummy
