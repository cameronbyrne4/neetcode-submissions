# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        given 2 nodes in the tree, find the lowest common ancestor

        IDEAS: it will be p<= LCA <= q
        -- could just do binary search to make a list of the path, then see what matches?
        -- aka pick the largest matching

        WHY DOES IT KIND OF SEEM LIKE THE FIRST VALUE THAT ITS BETWEEN
        '''
        # make p < q
        p1 = p.val
        q1 = q.val
        if p1 > q1:
            p1,q1 = q1,p1

        # bs
        while root.val < p1 or root.val > q1:
            if root.val < p1:
                root = root.right
            else:
                root = root.left
        return root