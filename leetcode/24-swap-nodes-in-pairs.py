# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        while prev.next and prev.next.next: # prev->a->b->c to prev->b->a->c
            a, b, c = prev.next, prev.next.next, prev.next.next.next
            prev.next, b.next, a.next, prev = b, a, c, a
        return dummy.next