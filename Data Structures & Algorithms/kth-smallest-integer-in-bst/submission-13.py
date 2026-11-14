# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # might have to traverse entire tree?
        # if we do inorder it should be fine right???
        
        i = 0
        res = -1

        def search(node) -> None:
            nonlocal i
            nonlocal res
            if not node:
                return
            
            search(node.left)
            i += 1
            # print("node val", node.val)
            if i == k:
                res =  node.val
            search(node.right)
        search(root)
        return res

        

        