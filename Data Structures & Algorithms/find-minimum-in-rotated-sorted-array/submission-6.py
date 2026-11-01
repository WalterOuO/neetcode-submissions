class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1 
        if nums[l] <= nums[r]:   # 代表沒rotated過
            return nums[l]

        res = nums[0]
        while l <= r:
            m = (l+r) // 2

            # [4, 5, 6, 7, 0, 1, 2]
            #              l  m  r
            if nums[l] <= nums[r]:  # l改變後若變有序, min一定是l不是m
                res = min(res, nums[l])
                break

            res = min(res, nums[m]) # compare m first
            # left side is sorted: minimum is in right side
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res
