class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # understand: return idx(i,j),  i!=j,  nums[i]+nums[j]=target
        # brute force: nested for loop : Time complx is O(n^2)
        # alternative: search if (target-nums[i]) in nums, use hashmap
        # search cost O(1), for loop O(n)*O(1) = O(n)
        # hashmap key= nums[i], val= i
        seen = {}

        for i, val in enumerate(nums):
            rest = target - val
            if rest in seen and seen[rest] != i:
                return [seen[rest], i]
            seen[val] = i
        
        # Time: O(n) for loop * O(1) fill in / search idx in hashmap
        # Space: if len(nums) == n, O(n) for hashmap 
