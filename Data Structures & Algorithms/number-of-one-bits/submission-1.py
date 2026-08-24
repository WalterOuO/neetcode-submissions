class Solution:
    def hammingWeight(self, n: int) -> int:
        # Features of logic sum
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res