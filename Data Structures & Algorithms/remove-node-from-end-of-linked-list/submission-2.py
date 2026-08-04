# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        # build the distance between two pointer
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        # sliding two pointer
        while fast:
            slow = slow.next
            fast = fast.next
        # delete node
        slow.next = slow.next.next
        return dummy.next