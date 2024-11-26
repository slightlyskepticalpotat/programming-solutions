# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.ans = -float("inf")
        self.helper(root)
        return self.ans

    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = max(0, self.helper(root.left)), max(0, self.helper(root.right))
        self.ans = max(self.ans, left + right + root.val)
        return max(left, right) + root.val