class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2, 3, 4, 5] 
        # when find 2, continuing find 3, 4, 5. store the max_len
        # [2, 2, 4, 3, 3, 5, 4, 6, 10, 13] -> set [2, 3, 4, 6, 10, 13]
        # [2, 3, 6, 7, 4, 8, 5]
        max_len = 0
        n_set = set(nums)
        for n in nums:
            if (n-1) not in n_set:
                length = 0
                while (n + length) in n_set:
                    length += 1
                max_len = max(max_len, length)
        return max_len

        # Time: O(n) for loop, searching set cost O(1)
        # Space: O(n) for n_set