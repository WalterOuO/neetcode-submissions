"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Two pointers
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s_ptr = e_ptr = 0
        rooms = 0

        while s_ptr < len(intervals):
            # 如果下一個會議開始時，最快結束的會議還沒結束 -> 需要加開房間
            if starts[s_ptr] < ends[e_ptr]:
                rooms += 1
            else:
                # 有房間空出來了，讓結束指標往後移
                e_ptr += 1
            s_ptr += 1

        return rooms