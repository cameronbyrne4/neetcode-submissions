# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def isLeafTarget(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if not root.left and not root.right and root.val == target:
                return True
            else:
                return False

        if not root:    # base case
            return

        # Process AFTER movement because we are postorder
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if isLeafTarget(root):
            return None
        
        return root
