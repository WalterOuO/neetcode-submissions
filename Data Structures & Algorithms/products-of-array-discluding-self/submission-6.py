class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Greedy
        output = [1] * len(nums)

        # [1,     2,     4,     6]
        # [2*4*6, 1*4*6, 1*2*6, 1*2*4]
        # [1,     1,     1,     1]
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        
        return output

        # Time: O(n)
        # Space: O(n)