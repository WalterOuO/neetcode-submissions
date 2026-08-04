# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointer: to locate "the node before removed node"
        # make distance of two pointer = n+1 (left pointer)
        dummy = ListNode(0, head)
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1

        # shift left pointer to "the node before removed node"
        while right:
            right = right.next
            left = left.next
        
        # delete the removed node
        left.next = left.next.next
        return dummy.next