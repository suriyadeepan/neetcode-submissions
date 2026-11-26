# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # go to the end of list while keeping track of prev
        dummy = ListNode(next=head)
        l, r = dummy, dummy
        for _ in range(n):
            r = r.next
        
        while r.next:
            r = r.next
            l = l.next

        # switch connection
        l.next = l.next.next

        return dummy.next