# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        if not root:
            return list(res.values())
        layer = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                res[layer].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            layer += 1

        return list(res.values())
