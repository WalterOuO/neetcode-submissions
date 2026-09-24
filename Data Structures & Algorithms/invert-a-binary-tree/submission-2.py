# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # stop criteria
        if not root:
            return 

        # exchange left, right node
        tmp = root.left
        root.left = root.right
        root.right = tmp    

        # recursion
        self.invertTree(root.left)
        self.invertTree(root.right)        
        
        return root

        # # Review:
        # 1 3 2-> self.invertTree(3) -> 3
        # -> 3 7 6 -> self.invertTree(7), self.invertTree(6)
        # -> self.invertTree(2) -> 2
        # -> self.invertTree(5), self.invertTree(4)
        # 1
        
        # # Evaluation
        # Time: n * O(1) = O(n)
        # Space: h = logn (best case), n (worst case) -> O(n) 