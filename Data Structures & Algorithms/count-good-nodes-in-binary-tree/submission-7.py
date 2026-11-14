# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # I think this is DFS
        # track the max value in each traversal, and compare that to the current one
        self.res = 0
        
        def dfs(x, currMax):
            if not x:
                return None
            if x.val >= currMax:
                currMax = x.val # should we make this a global var?
                self.res +=1
            

            dfs(x.left, currMax)
            dfs(x.right, currMax)


        dfs(root,root.val)
        return self.res