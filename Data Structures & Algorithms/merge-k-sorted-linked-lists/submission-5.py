# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Interval Method: reduce Space complexity to O(1)
        if not lists:
            return None

        interval = 1        # enable O(1) space complexity

        while interval < len(lists):
            # 每次跨過 2 * interval 的步長
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])

            # 跨步翻倍：1 -> 2 -> 4 -> 8 ...
            interval *= 2

        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next