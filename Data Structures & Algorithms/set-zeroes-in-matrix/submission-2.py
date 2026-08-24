class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return 
        # O(1) solution
        row, col = len(matrix), len(matrix[0])
        # just need one variable: zero
        rowzero = False

        # determine which rows/cols to zero out
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r != 0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True
                
        # change to zero, skip 1st row, 1st col to avoid repeating change
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
        if rowzero:
            for i in range(col):
                matrix[0][i] = 0

