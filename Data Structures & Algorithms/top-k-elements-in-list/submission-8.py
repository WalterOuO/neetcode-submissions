class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # create a bucket List(List), idx is freq(1~n), val is n
        # [ [], [], [] ....., [] 需要 len(nums)+1 個] 因為頻率只從1開始~n
        bucket = [[] for i in range(len(nums) + 1) ]
        
        for n, freq in count.items():
            bucket[freq].append(n)
        
        res = []
        for i in range(len(bucket) -1, 0, -1 ):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        # if len(nums) = n
        # Time: at most O(n) for counter + at most O(n) for filling bucket + at most n times for filling res = O(n)
        # Space: at most O(n) for Counter, at most O(n) for bucket, at most O(n) for res
            