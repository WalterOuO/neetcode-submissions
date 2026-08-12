class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # BFS
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in DIR:
                    r, c = row + dr, col + dc
                    if (0 <= r < ROWS and 
                        0 <= c < COLS and
                        grid[r][c] == "1" ):
                        q.append((r, c))
                        grid[r][c] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    island += 1
        return island