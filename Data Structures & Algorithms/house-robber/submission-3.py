class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2,    1, 2, 3...
        #       rob1, rob2, 2, 3
        # if 2 > 1+3:

        # curmax, lastmax = 0, 0
        # for n in nums:
        #     temp = max(curmax + n, lastmax)
        #     curmax = lastmax
        #     lastmax = temp

        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
