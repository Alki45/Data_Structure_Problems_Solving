# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,node,ans):
        if not node:
            ans.append(None)
            return
        ans.append(node.val)
        self.preorder(node.left,ans)
        self.preorder(node.right,ans)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_ans = []
        p_ans = []

        self.preorder(q,q_ans)
        self.preorder(p,p_ans)
        if q_ans == p_ans:
            return True
        return False
        