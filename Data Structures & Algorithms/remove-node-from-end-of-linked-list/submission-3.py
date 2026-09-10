# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # slow, fast pointer: distance == n
        # None, 1, 2, 3, 4, None
        # None, 5
        #   |  n+1   
        #          |
        #

        # key point: create a dummy so that we can return dummy.next
        dummy = ListNode(0, head)
        first = second = dummy
        while n+1:
            second = second.next
            n -= 1
        
        # now first pointer move to the removed one
        # need first to pointer the previous one
        while second:
            first = first.next
            second = second.next
        # now first = prev, second = None
        first.next = first.next.next

        return dummy.next
