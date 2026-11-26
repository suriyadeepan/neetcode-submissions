# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # save next node
            next = curr.next
            # connect curr to previous
            curr.next = prev
            # move prev one step right
            prev = curr
            # move curr one step right: point curr to saved next node
            curr = next

        return prev

        