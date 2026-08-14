class MedianFinder:
    # heap 
    def __init__(self):
        
        # Two heap: small side, large side
        # max heap for small value
        # min heap for large value
        # return max of small, min of large to calculate median

        # Why heap not array? add,remove num into array:O(n), heap is O(logn)
        self.small, self.large = [], []


    def addNum(self, num: int) -> None:
        '''
        Python view heap as min heap as default
        so to build MAX HEAP, need reverse the number by * -1
        '''
        heapq.heappush(self.small, -1 *num) # max heap of small side

        # if small side have value larger than large side, than switch it
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # small side at most 1 more num than large side, cannot 2, 3.. more
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 *val)


    def findMedian(self) -> float:
        # if odd num: pop the heap that have more value
        # if even num: pop both heap to average count median

        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2