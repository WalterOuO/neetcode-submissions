class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:      # means min is in right side
                l = m + 1
            else:                       # means min is in left side
                r = m - 1

        return res

        # Evaluation
        ## Time: O(logn), Space: O(1)