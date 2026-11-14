# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        if not root:
            return []
        while q:
            curlen = len(q)
            curlist = []

            for i in range(curlen):
                curnode = q.popleft()
                curlist.append(curnode.val)
                if curnode.left:
                    q.append(curnode.left)
                if curnode.right:
                    q.append(curnode.right)
            res.append(curlist)
        return res
