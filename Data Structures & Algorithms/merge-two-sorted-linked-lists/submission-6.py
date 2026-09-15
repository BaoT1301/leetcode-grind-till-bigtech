# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val

            if val2 > val1:
                tail.next = ListNode(val1)
                list1 = list1.next
            else:
                tail.next = ListNode(val2)
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

