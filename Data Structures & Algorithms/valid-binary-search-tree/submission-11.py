# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
want to check children of every node
if kids are good
    we go to them

Confirming kids are good:
    -dfs has upper and lower bounds for it
    -can update when we call dfs to be min or max

    go right -> make it the min
    go left -> max it the max

Output bool
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True # single node

        def dfs(r, mi, ma):
            # Ending conditions
            if not r:
                return True
            print(type(mi), type(r.val), type(ma))
            if not (mi < r.val < ma):
                return False

            # repeat conditions
            return all((dfs(r.left, mi, r.val), dfs(r.right, r.val ,ma)))


        mi = -1111
        ma = 1111
        return dfs(root, mi, ma)



