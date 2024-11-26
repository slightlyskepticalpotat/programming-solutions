# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                rightmost = root.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = root.right
                root.right, root.left = root.left, None
            root = root.right
# try not to nest code
# think about solution before implementing
# helper functions are good
# practice practice practice
# don't tunnel vision 
# many interviews won't run your code (syntax)
# be able to describe what your code does on given case
# think about time complexities
# generally bigger companies don't care except when role language-specific
# do research on company beforehand