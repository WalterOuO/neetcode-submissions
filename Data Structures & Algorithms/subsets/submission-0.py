class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def createset(layer):
            if layer == len(nums):
                res.append(subset[:])
                return 

            subset.append(nums[layer])
            createset(layer+1)
            subset.pop()
            createset(layer+1)

        createset(0)
        return res