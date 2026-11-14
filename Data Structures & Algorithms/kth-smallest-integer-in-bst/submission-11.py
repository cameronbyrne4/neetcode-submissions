# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        We want to explore it mid-order (not pre or post)
        just do normal exploration with tracking the number we've been to (in a global var)
        '''
        self.numexplored = 0
        def dfs(r) -> int:
            # cancel
            if not r:
                return None
            dl =  dfs(r.left)
            if dl:
                return dl
            # r exists
            self.numexplored += 1
            print(self.numexplored)
            if self.numexplored == k:
                print("solution found")
                return r.val
            
            dr = dfs(r.right)
            if dr:
                return dr

        return dfs(root)
