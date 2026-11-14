# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        # try to do bfs solution?

        # put root in q
        q = deque()
        q.append((root, float("-inf"), float("inf")))

        while q:
            # If we run into any troubles return false
            # Full processing means it's clean

            node, leftBound, rightBound = q.popleft()
            if not leftBound < node.val < rightBound: # assume unique vals
                return False
            if node.left:
                q.append((node.left, leftBound, node.val))
            if node.right:
                q.append((node.right, node.val, rightBound))
                
        return True