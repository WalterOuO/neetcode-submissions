class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m + n - 2
        K = min(m - 1, n - 1)

        res = 1
        for i in range(1, K + 1):
            res = res * (N - K + i) // i
        
        return res