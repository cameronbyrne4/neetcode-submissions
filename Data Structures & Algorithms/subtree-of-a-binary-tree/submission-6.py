# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        1. Go thru root tree until we match the starting values
            * return Flase if we cant find it
        2. then march left and right recursively
            * return True if we make it to the end of both
            * false if any mismatches
        '''
        def compare(root1, root2):
            # Exist
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            
            # Val
            if root1.val != root2.val:
                return False
            
            # Recurse
            # By now, both exist and have the same value
            return (compare(root1.left, root2.left) and compare(root1.right, root2.right))
        
        ans = False
        def trace(node): # traces thru root
            nonlocal ans
            if not node:
                return
            
            if node.val == subRoot.val:
                
                if compare(node, subRoot):
                    ans = True
            trace(node.left)
            trace(node.right)
        
        trace(root) # just updates ans
        return ans




