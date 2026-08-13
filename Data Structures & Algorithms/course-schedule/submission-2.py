class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        link = defaultdict(list)
        for [crs, pre] in prerequisites:
            link[crs].append(pre)
        
        
        visit = set()

        def dfs(c):
            if link[c] == []:
                return True
            if c in visit:
                return False

            visit.add(c)
            for i in link[c]:
                if not dfs(i): return False
            visit.remove(c)
            link[c] = []        # remove visited node
            return True           


        for n in range(numCourses):
            if not dfs(n): return False
        return True
