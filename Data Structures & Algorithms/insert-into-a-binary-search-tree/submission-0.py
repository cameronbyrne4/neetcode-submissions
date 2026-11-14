# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        * Add to the top and bubble down? no that's for balanced this is easier. we can just add it whever
        '''
        
        cur = root  #for traversal
        new = TreeNode(val)
        if not root:
            return new
        while cur:
            if cur.val < val:
                # move rihgt if there is a right child, or else just slot it in
                if not cur.right:
                    cur.right = new
                    return root
                else:
                    cur = cur.right
                    
            
            else:
                if not cur.left:
                    cur.left = new
                    return root
                else:
                    cur = cur.left

   