# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # have cycle: [1, 2, 3, 4, 2, 3, 4, 2, 3, 4,...]
        # [1,2,3,4,2,3,4,2,3,4,...]
        #      |
        #            |
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        
        # Time: O(n)
            # No cycle: fast walk n/2 times
            # Has cycle: fast walk at most 2n times 
        # Space: O(1) constant variable

