class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        if len(word) > ROWS * COLS:
            return False
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] != word[i]):
                return False
            # switch path block to #, no need call stack anymore
            temp = board[r][c]
            board[r][c] = "#"

            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
            # backtrack
            board[r][c] = temp
            return res

        for r in range(ROWS):
            for c in range(COLS):
                # Start DFS only when we find the first word
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
