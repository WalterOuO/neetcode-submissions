class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair :pair[0])
        res = []
        miv = intervals[0][0]
        mav = intervals[0][1]
        for i in range(len(intervals)):
            if miv <= intervals[i][0] <= mav:
                miv = min(miv, intervals[i][0])
                mav = max(mav, intervals[i][1])
            elif mav < intervals[i][0]:
                res.append([miv, mav])
                miv = intervals[i][0]
                mav = intervals[i][1]
                
        if i == len(intervals) - 1:
            res.append([miv, mav])
        return res