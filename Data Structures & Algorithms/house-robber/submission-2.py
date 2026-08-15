class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programming
        # rob2 = last house we rob
        # rob1 = last house we rob before rob "rob2"
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)  # left + right vs. middle
            rob1 = rob2
            rob2 = temp
        return rob2