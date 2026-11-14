# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        bfs but we only take the last one in the sequence
        '''

        q = deque()
        res = []
        if not root:
            return []
        
        # root exists
        q.append(root)

        while q:
            n = len(q)
            for i in range(len(q)):
                # add left and right to q
                # if last one, appned
                cur = q.popleft()
                if i == n-1:
                    res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res

