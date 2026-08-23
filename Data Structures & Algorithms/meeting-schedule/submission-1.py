"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        bigend = intervals[0].end
        for n in intervals[1:]:
            if n.start < bigend:
                return False
            else:
                bigend = max(bigend, n.end)
        return True