class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def countone(n):
            count = 0
            while n:
                count += n % 2
                n = n >> 1
            return count

        for i in range(n+1):
            res.append(countone(i))
        return res


        