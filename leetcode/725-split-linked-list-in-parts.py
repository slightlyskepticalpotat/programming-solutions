# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(head):
        if not head:
            return 0
            
        ans = 0
        while head := head.next:
            ans += 1
        return ans + 1

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        min_len, extra = divmod(Solution.length(head), k)

        for i in range(k):
            cur_head = head
            for j in range(min_len - 1 + (i < extra)):
                head = head.next 
            if head:
                next = head.next
                head.next = None
                head = next
            ans.append(cur_head)
        return ans