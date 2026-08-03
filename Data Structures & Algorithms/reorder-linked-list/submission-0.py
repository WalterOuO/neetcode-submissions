# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow and fast pointer to find middle and split list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next        # slow pointer will stop at middle of list
            fast = fast.next.next

        # split the list
        second = slow.next
        prev = slow.next = None # end 1st list and add start of 2nd list with None
        # reverse the 2nd list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # when while loop stop, prev = end of list, slow = None
        
        # start to merge two list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
