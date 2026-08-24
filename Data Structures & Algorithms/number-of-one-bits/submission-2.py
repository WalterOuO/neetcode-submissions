class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary feature
        res = 0
        while n:
            res += n % 2
            n = n >> 1  # right shift 1 space
        return res