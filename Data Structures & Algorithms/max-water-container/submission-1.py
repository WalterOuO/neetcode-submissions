class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        maxarea = 0
        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                area = (r - l)* min(heights[l], heights[r])
                maxarea = max(maxarea, area)
        return maxarea

        # two pointers 
        #l, r = 0, len(heights) - 1