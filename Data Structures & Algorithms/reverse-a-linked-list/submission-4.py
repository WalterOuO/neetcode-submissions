# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3 -> None
        # None <-0  1-> 2-> 3-> None

        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        return prev