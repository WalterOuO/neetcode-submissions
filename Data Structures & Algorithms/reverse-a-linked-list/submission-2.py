# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive: T O(n), M O(n)

        if not head:    # stop criteria for recursion: stop if head is Null
            return None
        
        newHead = head
        if head.next is not None:                 # 假設現在在 1
            newHead = self.reverseList(head.next) # 叫遞迴去把 2 後面的東西反轉好
            head.next.next = head       # 2的下一個是Null，Null的指標指回2
        head.next = None                # 切斷 2 指向下一個的指標

        return newHead