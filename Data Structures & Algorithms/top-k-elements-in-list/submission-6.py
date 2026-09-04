class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm = defaultdict(int)
        for n in nums:
            hashm[n] += 1
        heap = []
        for key, val in hashm.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:     
                heapq.heappop(heap)
        
        return [n for _, n in heap]