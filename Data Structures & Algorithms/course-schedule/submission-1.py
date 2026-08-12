class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # UMPIRE
        # Understand:
        # a) In the first case, numCourses mean there're 2 courses that I need to take, and I only have to take course 1, so 1 < 2  is available, right?
        # b) In the second case, no matter how many numCourses are, it will never available, right?
        relation = defaultdict(list)
        for [course, pre] in prerequisites:
            relation[course].append(pre)

        visit = set()

        def dfs(i):
            if i in visit:
                return False
            if relation[i] == []:
                return True
            
            visit.add(i)
            for n in relation[i]:
                if not dfs(n): return False
            visit.remove(i)
            relation[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
 