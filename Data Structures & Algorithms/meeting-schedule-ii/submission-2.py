"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Greedy
        time = []
        
        for n in intervals:
            # view start as 1, end as -1, all over must be 0, 
            # so current sum must be room number
            time.append( (n.start, 1) )
            time.append( (n.end, -1) )
        
        time.sort(key=lambda x: (x[0], x[1]))

        res = cur = 0
        for t in time:
            cur += t[1]
            res = max(res, cur)
        
        return res