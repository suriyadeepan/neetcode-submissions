# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        
        head = ListNode()
        tail = head

        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                tail = p1
                p1 = p1.next
            else:
                tail.next = p2
                tail = p2
                p2 = p2.next

        if p2 and not p1:
            tail.next = p2
            
            
        if p1 and not p2:
            tail.next = p1
            
        return head.next
            

