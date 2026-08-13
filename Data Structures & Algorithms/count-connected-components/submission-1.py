class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n or n == 0:
            return 0
        
        # like island problem

        # link the edges
        link = {i: [] for i in range(n)}
        for p, q in edges:
            link[p].append(q)
            link[q].append(p)

        visit = set()
        part = 0
        # dfs to go through link
        def dfs(n, pre):
            visit.add(n)
            for i in link[n]:
                if i == pre:
                    continue
                if i not in visit:
                    dfs(i, n)
            return 

        # search from 0-> n-1, skip those already visit
        for node in range(n):
            if node not in visit:
                dfs(node, -1)
                part += 1
            
        return part