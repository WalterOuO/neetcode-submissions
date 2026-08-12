class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # BFS + deque
        def bfs(r, c, oceanset):
            q = deque([(r, c)])
            oceanset.add((r, c))
            while q:
                row, col = q.popleft()
                cur = heights[row][col]
                for dr, dc in DIR:
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
        return [list(point) for point in (pacific & atlantic)]
        # Evaluation
        ## Time: O(M*N): each point only enter oceanset once, so at most M*N times
        ## Space: O(M*N) at most store every point on the map