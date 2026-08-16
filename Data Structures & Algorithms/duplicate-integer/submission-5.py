class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if hashmap.get(n,0) > 0:
                return True
            hashmap[n] = hashmap.get(n, 0) +1
        return False