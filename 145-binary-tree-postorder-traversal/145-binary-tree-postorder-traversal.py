# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.helper(root)
        
        return self.ans
    
    def helper(self,root:Optional[TreeNode]):
        if root is None:
            return
        self.helper(root.left)
        self.helper(root.right)
        self.ans.append(root.val)