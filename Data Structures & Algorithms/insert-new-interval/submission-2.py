class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # 2-4, 7-9, 12-14
        # 0-1  case1
        # 5-6  case2
        # 4-7  case3

        for i in range(len(intervals)):
            
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # update newInterval
                newInterval = [min(intervals[i][0], newInterval[0]), 
                 max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res
                