class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                row, col = q.popleft()
                for dr, dc in DIR:
                    r, c = row + dr, col + dc
                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                        grid[r][c] != "1"):
                        continue
                    q.append((r, c))
                    grid[r][c] = "0"
                    if (0 <= r < ROWS and
                        0 <= c < COLS and
                        grid[r][c] == "1"):
                        q.append((r, c))
                        grid[r][c] = "0"
            return 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    island += 1
        return island

                
               