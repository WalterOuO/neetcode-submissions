class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min-heap
        n_map = defaultdict(int)
        for n in nums:
            n_map[n] += 1
        
        heap = []
        for i, val in n_map.items():
            heapq.heappush(heap, (val, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for i, n in heap]