# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # q is the larger one
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        
        def dfs(root, p, q):
            if not root:
                return
            print(p.val, root.val, q.val)
            if p.val <= root.val <= q.val:
                print("answer found")
                return root     # ANSWEr
            
            if root.val > q.val:
                # go left
                return dfs(root.left, p, q)
            else:
                return dfs(root.right, p, q)
        val= dfs(root,p,q)
        print(val)
        return val
