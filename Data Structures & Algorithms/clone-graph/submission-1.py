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
            if node in oldtonew:
                # return new one to build connection
                return oldtonew[node]
            
            copy = Node(node.val)
            oldtonew[node] = copy
            # build connection
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) # recursion to clone all node
            return copy
        return dfs(node) if node else None