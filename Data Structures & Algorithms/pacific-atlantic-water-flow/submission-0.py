class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        # BFS + deque
        def bfs(r, c, oceanset):
            q = deque([(r, c)])
            oceanset.add((r, c))
            while q:
                row, col = q.popleft()
                cur = heights[row][col]
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows and 
                        0 <= c < cols and
                        heights[r][c] >= cur and
                        (r, c) not in oceanset):
                        q.append((r, c))
                        oceanset.add((r, c))


        # pacific
        for r in range(rows):
            bfs(r, 0, pacific)
        for c in range(cols):
            bfs(0, c, pacific)

        # atlantic
        for r in range(rows):
            bfs(r, cols - 1, atlantic)
        for c in range(cols):
            bfs(rows - 1, c, atlantic)
        
        # find common points in both set
        common = []
        for point in pacific:
            if point in atlantic:
                common.append(point)
        return [list(point) for point in common]