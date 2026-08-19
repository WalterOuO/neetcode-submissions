class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Combinations
        return math.comb(m + n - 2, m - 1)