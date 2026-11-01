class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # use binary search seperately: two sorted list
        # brute force
        i, j = 0, 0
        nums = []
        # [1, 3], [2, 4]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            nums += nums1[i:]
        elif j < len(nums2):
            nums += nums2[j:]
        # [1, 2, 3, 4]
        k = len(nums)
        if k % 2 == 0: # 偶數
            return ( nums[(k//2) -1] + nums[k//2]) /2
        else:
            return nums[k//2]
        
        # Evaluation
        ## Time O(m+n)
        ## Space O(m+n)

