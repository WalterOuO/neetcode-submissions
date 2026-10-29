class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height = [1, 7, 2, 5, 4, 7, 3, 6]
        l, r = 0, len(heights)-1
        area = 0
        
        while l < r:
            new_area = min(heights[l], heights[r]) * (r - l)
            area = max(area, new_area)
            # greedy: left max height
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return area