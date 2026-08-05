# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Bottom-up Method: Overwrite to reduce Space complexity to O(1)
        # Key Though: [L0, L1, L2, L3] 每次合併L0, L1後就用不到 L0, L1了，可覆寫掉
        if not lists:
            return None

        k = len(lists)

        # 只要剩餘的有效長度 k > 1，就繼續對半壓縮
        while k > 1:
            for i in range(0, k, 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < k else None

                # 關鍵：把合併結果直接存回 lists[i // 2]，覆寫掉用過的list
                lists[i // 2] = self.merge(l1, l2)

            # 每一輪結束後，有效的 list 數量直接砍半 = 將後半沒被覆寫的捨去
            # 原本是 [1, 2, 3, 4, 5]
            # 覆寫後 [(1+2), (3+4), 5, 4, 5] , so k+1 = 6, 6//2 = 3
            k = (k + 1) // 2

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
    # Evaluation
    ## Time: O(NlogK)
    ## Space: no extra list created, so O(1)