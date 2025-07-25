# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        m=[]
        def solve(node,l,sm):
            if not node:
                return 
            l.append(node.val)
            if not node.left and not node.right and sm==node.val:
                m.append(l[:])
            else:
                solve(node.left,l,sm-node.val)
                solve(node.right,l,sm-node.val)
            l.pop()

        
        solve(root,[],targetSum)
        return m
        