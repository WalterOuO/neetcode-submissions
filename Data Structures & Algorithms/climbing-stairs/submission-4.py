class Solution:
    def climbStairs(self, n: int) -> int:
        # 0, 1, 2, 3, 4
        #          1, 1
        #       2, 1
        #    3, 2
        # 5, 3

        one, two = 1, 1
        for i in range(n-1):
            one, two = one+two, one
        return one