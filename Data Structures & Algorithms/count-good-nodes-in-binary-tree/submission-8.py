# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        DFS
        - root always good
        - Good = it's the largest in the path (path maintains that value)
        '''

        if not root:
            return 0

        self.output = 0

        def dfs(node, path_max):
            if not node:
                return
            if node.val >= path_max:
                # valid
                self.output += 1
                path_max = node.val
            if node.left:
                dfs(node.left, path_max)
            if node.right:
                dfs(node.right, path_max)

        dfs(root, root.val)
        return self.output