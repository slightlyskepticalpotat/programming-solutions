# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.path = []
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            self.path.append(root.val)
            in_order(root.right)
        in_order(root)
        return self.path[k - 1]