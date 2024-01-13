# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, cur = 0, head
        while cur.next:
            cur = cur.next
            n += 1
        
        n, cur = math.ceil(n / 2), head
        for i in range(n):
            cur = cur.next
        return cur