# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, sum, loc):
        if not root:
            return
        if not root.left and not root.right and sum == root.val:
            loc.append(root.val)
            self.ans.append(loc)
        self.dfs(root.left, sum - root.val, loc + [root.val])
        self.dfs(root.right, sum - root.val, loc + [root.val])

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self.dfs(root, targetSum, [])
        return self.ans