# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            mx = 1
            if root.left:
                mx = max(mx, dfs(root.left) + 1)
            if root.right:
                mx = max(mx, dfs(root.right) + 1)
            return mx
        return dfs(root)


     