# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(preorder.pop(0)) # location of root in inorder
            root = TreeNode(inorder[idx]) # create new root node
            root.left, root.right = self.buildTree(preorder, inorder[:idx]), self.buildTree(preorder, inorder[idx + 1:]) # left, right parts of inorder array
            return root