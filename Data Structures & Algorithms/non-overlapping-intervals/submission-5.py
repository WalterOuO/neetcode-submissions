class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:(x[0], x[1]))
        res = 0
        lastmax = intervals[0][1]
        for start, end in intervals[1:]:

            if start < lastmax:
                res += 1
                # Greedy: keep the one who have smaller length, 
                        # leaving more space for other interval
                lastmax = min(lastmax, end)
            else:
                lastmax = end

        return res