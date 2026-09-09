class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # understand: return idx(i,j),  i!=j,  nums[i]+nums[j]=target
        # brute force: nested for loop : Time complx is O(n^2)
        # alternative: search if (target-nums[i]) in nums, use hashmap
        # search cost O(1), for loop O(n)*O(1) = O(n)
        # hashmap key= nums[i], val= i
        hashnum = defaultdict(int)

        for i in range(len(nums)):
            hashnum[nums[i]] = i
        
        # search (use idx search)
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in nums and hashnum[rest] != i:
                return [i, hashnum[rest]]
