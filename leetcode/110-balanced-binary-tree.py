# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if  root is None:
                return True
            return max(height(root.left), height(root.right)) + 1
        
        def balanced(root):
            if root is None:
                return True
            h_l = height(root.left)
            h_r = height(root.right)
            return abs(h_l - h_r) < 2 and balanced(root.left) and balanced(root.right)
        
        return balanced(root)
        