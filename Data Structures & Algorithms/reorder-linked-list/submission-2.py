# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # None, 2, 4, 6
        # None, 2, 4, 6, 8
        #          |
        #                |

        # cut half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first = head
        second = slow.next
        slow.next = None
        
        # reverse second half
        prev, cur = None, second
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        second = prev

        # connect to head, in-place
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

