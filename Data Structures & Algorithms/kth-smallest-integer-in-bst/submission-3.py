# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # pre order, post order, in order
        # can count how many nodes are in each direction? and add it
        self.visitCount = 0
        def dfs(x, vali):
            

            if not x:
                return None
            dfs(x.left, vali)
            self.visitCount += 1
            if self.visitCount == vali:
                self.res = x.val

            dfs(x.right, vali)

        dfs(root, k)
        return self.res
