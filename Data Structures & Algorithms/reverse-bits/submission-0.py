class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # i & 1 can get the last bit
        # res | i can add bit into res

        for i in range(32):
            # as for loop going, get different bit of n
            getbit = (n >> i) & 1
            res = res | (getbit << (31-i)) # leftshift to add bit into res
        return res

