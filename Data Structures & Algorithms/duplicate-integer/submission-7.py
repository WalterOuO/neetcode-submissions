class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasht = defaultdict(int)
        for n in nums:
            hasht[n] += 1
            if hasht[n] > 1:
                return True
        return False