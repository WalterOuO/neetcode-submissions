"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Min-heap
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        min_heap = []

        for n in intervals:
            if min_heap and n.start >= min_heap[0]:
                heapq.heappop(min_heap) # remove the min one
            heapq.heappush(min_heap, n.end)
        
        return len(min_heap)