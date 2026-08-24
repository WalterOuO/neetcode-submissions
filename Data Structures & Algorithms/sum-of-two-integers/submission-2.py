class Solution:
    def getSum(self, a: int, b: int) -> int:
        # python int: have no max bit bound (unfinite)
        # Java int: signed int: 32 bits as bound (32 is sign)
        
        # Manually make Mask for python
        Mask = 0xFFFFFFFF
        Mask_limit = 0x7FFFFFFF  # (one 0 + 31 1)
        
        # sum = [(a) sum (b)] sum (shift carry)
        while b != 0:               # sum up until no carry
            dif = (a ^ b) & Mask             # adding
            carry = ((a & b) << 1) & Mask    # leftshift carry
            a = dif
            b = carry
        # 如果最終結果 a 的最高位是 1（大於 MAX_INT），代表它是負數
        # 要轉回 python 的負數表示法 ~a
        return a if a <= Mask_limit else ~(a ^ Mask)