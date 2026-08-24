class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        res = []


        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return 

            for i in range(col):
                c += dc
                r += dr
                res.append(matrix[r][c])

            # rotate the image
            dfs(col, row-1, r, c, dc, -dr)
        
        dfs(m, n, 0, -1, 0, 1)
        return res