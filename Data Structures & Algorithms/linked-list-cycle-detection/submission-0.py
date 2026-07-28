# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # UMPIRE
        # Understand: Is there any duplicate value in linked list? Yes
        # Match: hash table, fast and slow pointer
        # Plan: fast move 2 each step, slow move 1, faster will catch slow if cycle
        # Implement:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next        # move 1 for each step: slow pointer
            fast = fast.next.next   # move 2 for each step: fast pointer
            if slow == fast:
                return True
        return False