class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        store = set()
        for n in nums:
            store.add(n)
        for i in range(len(nums)+1):
            if i not in store:
                return i
