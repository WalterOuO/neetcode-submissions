class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n-1, -1, -1):
                # leave the right to allow: now = right + low
                if j == n-1: continue
                # now = right + low
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]