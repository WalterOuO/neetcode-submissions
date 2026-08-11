# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            # DFS
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        
        # pointer
        self.i = 0
        def dfs():
            if res[self.i] != "N":
                node = TreeNode(int(res[self.i]))
                self.i += 1
                node.left = dfs()
                node.right = dfs()
            else:
                self.i += 1
                return None
            return node
        return dfs()
            