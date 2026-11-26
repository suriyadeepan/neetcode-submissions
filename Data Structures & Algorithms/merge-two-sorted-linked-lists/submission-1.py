# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode() # dummy head
        tail = head

        while list1 and list2:
            if list1.val <= list2.val:
                # connect tail to list1
                tail.next = list1
                # move tail
                tail = list1
                # move list1 one step
                list1 = list1.next
            else:
                # connect tail to list2
                tail.next = list2
                # move tail
                tail = list2
                # move list2 one step
                list2 = list2.next
        
        # we run out of list2
        if list1 and not list2:
            # tether tail to list1
            tail.next = list1
        
        # we run out of list 1
        if list2 and not list1:
            # tether tail to list2
            tail.next = list2

        return head.next 
            




