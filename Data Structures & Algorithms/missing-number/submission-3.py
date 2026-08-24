class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Gauss sum
        total = numsum = 0
        for i in range(len(nums)+1):
            total += i
            if i < len(nums): numsum += nums[i]
        return total - numsum