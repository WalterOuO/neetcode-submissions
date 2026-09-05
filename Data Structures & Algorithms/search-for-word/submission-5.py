class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking
        if not board:
            return False
        
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if not ( 0 <= r < rows and 0 <= c < cols and
                board[r][c] == word[idx]):
                    return False
            temp = board[r][c]
            board[r][c] = "#"
            res =  (dfs(r + 1, c, idx+1) or
                    dfs(r - 1, c, idx+1) or
                    dfs(r, c + 1, idx+1) or
                    dfs(r, c - 1, idx+1)
                    )
            board[r][c] = temp
            return res

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False