class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 
        total = 0
        maxsum = nums[0]
        
        for n in nums:
            if total < 0:
                total = 0
            total += n
            maxsum = max(maxsum, total)

        return maxsum