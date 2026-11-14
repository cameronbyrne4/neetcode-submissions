# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # can this just be BFS but add the last on in the list to to the result?
        r = []

        q = collections.deque()
        if not root:
            return r
        q.append(root)

        # Stop when q is empty === when we go thru every node
        while q:
            #level = [] # we wont need this since we only using one
            currlen = len(q)
            for i in range(currlen):
                node = q.popleft()
                if node:
                    if node.left: 
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    # append rightmost of the level
                    if i == currlen - 1:
                        r.append(node.val)

        return r
