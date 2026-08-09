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
        ## Time: create hashmap O(n), index hashmap O(1), sending l,r index 
        ## will not copy list, so sending index is n node*O(1) => O(n)
        ## hashmap O(n) + send index O(n) = O(n)
        
        ## Space: O(n) for storing indices in hashmap, 
        ## Call stack: 平衡樹O(logn), 全單邊樹O(n), so still O(n)
       