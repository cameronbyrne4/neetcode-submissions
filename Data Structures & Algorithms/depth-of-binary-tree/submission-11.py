# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        do dfs, at the end of each run compare the depth (++ each dfs)
        '''
        
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        
        def dfs(r):
            # return 0 at the very end
            if not r:
                return 0
            
            # otherwise increment depth and see if it overcomes the max
            return max( 1 + dfs(r.left),1 + dfs(r.right) )
        
        return dfs(root)