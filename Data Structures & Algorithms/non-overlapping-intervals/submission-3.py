class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:(x[0], x[1]))
        res = 0
        mav = intervals[0][1]
        for start, end in intervals[1:]:

            if start < mav:
                res += 1
                # Greedy: remove the one who take too much length, 
                        # leaving more space for other interval
                mav = min(mav, end)
            else:
                mav = end

        return res