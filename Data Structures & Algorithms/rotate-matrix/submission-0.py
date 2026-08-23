class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse and Transpose
        rows, cols = len(matrix), len(matrix[0])

        # Reverse
        for r in range(rows):
            for c in range(0, cols//2):
                matrix[r][c], matrix[r][cols-c-1] = matrix[r][cols-c-1], matrix[r][c]
        
        # Transpose
        for r in range(rows):
            for c in range(0, cols-r):
                matrix[r][c], matrix[rows-c-1][cols-r-1] = matrix[rows-c-1][cols-r-1], matrix[r][c]