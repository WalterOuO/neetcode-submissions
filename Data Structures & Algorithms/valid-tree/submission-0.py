class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # understand: is all tree start from n = 0 (root = 0)?

        # Eligible Tree: 
        # 1) edges number must = n - 1
        # 2) no cycle

        if len(edges) != n - 1:
            return False
        
        # relation = {[] for i in range(n)}
        relation = defaultdict(set)
        for [root, chil] in edges:
            relation[root].add(chil)
            relation[chil].add(root)    # undirected edge: make link for both side

        seen = set()

        def dfs(p, prev):
            if p in seen:
                return False

            seen.add(p)
            for child in relation[p]:
                if child == prev: continue
                if not dfs(child, p): return False
            return True

        if not dfs(0, -1): return False
        return len(seen) == n