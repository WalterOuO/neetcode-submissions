# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        # dfs: 
        def dfs(node, dep):
            if not node:
                return 
            
            self.depth = max(self.depth, dep+1)
            
            dfs(node.left, dep + 1)  
            dfs(node.right, dep + 1)
        
        dfs(root, 0)
        return self.depth

        # Evaluation
        # Time: O(n) traverse all node once
        # Space: Worst Case(Skewed Tree) -> dfs: n layer: call stack: O(n)