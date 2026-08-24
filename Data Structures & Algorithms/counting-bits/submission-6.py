class Solution:
    def countBits(self, n: int) -> List[int]:
        # bit manipulation
        res = [0] * (n+1)
        for i in range(1, n+1):
            num = i
            while num != 0:
                res[i] += 1
                num &= (num - 1)
        return res
        # Evaluation
        ## Time: O(nlogn): n * while loop:O(logn)
        ## Space: O(n) for res