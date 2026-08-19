class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy: no need to solve to end, simplify problem
        goal = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                # shift the goal
                goal = i
            
        return True if goal == 0 else False