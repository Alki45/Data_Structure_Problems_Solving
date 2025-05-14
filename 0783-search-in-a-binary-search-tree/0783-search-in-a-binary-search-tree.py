# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searching(self,node, target):
        if not node:
            return None
        if node.val == target:
            return node
        if node.val == target:
            return node
        if node.val > target:
            return self.searching(node.left,target)
        if node.val < target:
            return self.searching(node.right,target)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        return self.searching(root, val)
