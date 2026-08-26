class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dig = set()
        for n in nums:
            dig.add(n)
        res = 0
        for n in nums:
            if (n-1) not in dig:
                length = 0
                while (n + length) in dig:
                    length += 1
                res = max(res, length)
        
        return res