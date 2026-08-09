# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hashmap + DFS
        indices = {val:i for i, val in enumerate(inorder)}
        
        self.idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.idx]
            self.idx += 1
            root = TreeNode(root_val)

            rootidx = indices[root_val]
            root.left = dfs(l, rootidx - 1)
            root.right = dfs(rootidx +1, r)
            return root
        
        return dfs(0, len(inorder) - 1)

        # Evaluation
        ## Time: using hash map cause n space, but reduce O(n) time for .index
        ## Space: O(n) for storing indices in hashmap
        