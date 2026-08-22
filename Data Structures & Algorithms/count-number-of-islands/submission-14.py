class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        
        # sent r, c
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                grid[r][c] != "1"):
                return None
            
            grid[r][c] = '0'
            res = ( dfs(r + 1, c) or
                    dfs(r - 1, c) or
                    dfs(r, c + 1) or
                    dfs(r, c - 1) )

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island += 1

        return island