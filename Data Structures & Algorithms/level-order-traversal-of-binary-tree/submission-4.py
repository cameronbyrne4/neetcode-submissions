# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Learning how to implement BFS
        # BFS:
            # queue FIFO
            # when queue is empty we are done
            # then add the left then right kids
            # pop kids from queue and move to sublist

        r = [] # result array
        q = collections.deque() # how to initialize queue
        q.append(root)

        # ends when empty
        while q:
            q_length = len(q)
            level = [] # sub arrays for level
            for i in range(q_length):
                node = q.popleft() # does this save at the same time?
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                r.append(level)

        return r