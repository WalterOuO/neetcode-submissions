class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        # [3, 5, 6, 9]     target = 11, res = [1, 2]
        # [3, 5, 6, 7, 9]  target = 11, res = [1, 2] 
        #  1           r
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]