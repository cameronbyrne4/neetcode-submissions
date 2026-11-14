# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Run DFS recursively on left and right to cover everything
        # global variable called "res"
        # each node tries to update it! compare to max height of l + r

        self.res = 0 # Creates it as a member variable so I can use it inside the dfs function

        # Nested function:
        def dfs(curr): # Passing in variable curr --> returns height
            if not curr:
                return 0
            
            # update max diameter
            self.res = max(self.res, dfs(curr.left) + dfs(curr.right))

            return 1 + max(dfs(curr.left),dfs(curr.right))
        
        dfs(root) # DONT FORGET TO ACTUALLY CALL THE FUNCTION
        return self.res