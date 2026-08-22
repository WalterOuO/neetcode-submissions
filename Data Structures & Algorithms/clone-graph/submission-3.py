"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # use hashmap to clone old graph to new graph 
        oldtonew = {}

        def dfs(node):
            # reuse the build node when meet it second time
            if node in oldtonew:
                return oldtonew[node]
            
            root = Node(node.val)
            # use hashmap to recode seen node
            oldtonew[node] = root
            
            # build connection
            for n in node.neighbors:
                root.neighbors.append(dfs(n))

            return root

        return dfs(node) if node else None