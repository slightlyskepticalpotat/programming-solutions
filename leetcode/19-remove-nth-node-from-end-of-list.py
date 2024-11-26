# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        for i in range(n):
            r = r.next
        if not r: # at end of array
            return head.next
        while r.next:
            l, r = l.next, r.next
        l.next = l.next.next # remove array
        return head