class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) -1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            
            # 不要判斷是否rotated過，因為重點在有rotated過的計算
            # 切兩半確認左右哪邊有排序(有排序的那邊可使用binary search)
            # target在其中就縮, 不在就換邊

            # left side is ordered
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1 
            # right side is ordered
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1