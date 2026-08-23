class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse and Transpose
        n = len(matrix)

        # Reverse
        for r in range(n):
            for c in range(0, n//2):
                matrix[r][c], matrix[r][n-c-1] = matrix[r][n-c-1], matrix[r][c]
        
        # Transpose
        for r in range(n):
            for c in range(0, n-r):
                matrix[r][c], matrix[n-c-1][n-r-1] = matrix[n-c-1][n-r-1], matrix[r][c]