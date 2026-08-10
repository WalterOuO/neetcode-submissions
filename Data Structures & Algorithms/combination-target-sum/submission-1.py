class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def add(i, cur, total):
            if total == target:
                res.append(cur[:])
                return 
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            add(i, cur, total + nums[i])
            cur.pop()
            add(i+1, cur, total)
        
        add(0, [], 0)
        return res