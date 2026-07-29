class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:                   # must have '='

            m = (l + r) // 2

            if nums[m] == target:
                return m 

            # left array is ordered
            if nums[l] <= nums[m]:      # must have '='
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right array is ordered
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1