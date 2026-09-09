class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency problem
        # min-heap: if len(heap) > k: pop out
        count = Counter(nums)
        heap = []
        for pairs in count.items():
            heapq.heappush(heap, (pairs[1], pairs[0]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [n for _,n in heap]
        
        # return [num for num, _ in Counter(nums).most_common(k)]

        # if len(nums) = n, m unrepeated nums , max_len of heap = k
        # Time: O(n) for Counter, O(m) for loop * O(logk) heappush/pop = O(nlogk)
        # Space: O(n) for count + O(k) = O(n+k) = O(n)
