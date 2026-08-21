class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def add(i, mylist, total):
            if total == target:
                res.append(mylist[:])
                return 
            if i >= len(nums) or total > target:
                return 
            
            mylist.append(nums[i])
            add(i, mylist, total + nums[i])
            mylist.pop()
            add(i + 1, mylist, total)

        add(0, [], 0)
        return res