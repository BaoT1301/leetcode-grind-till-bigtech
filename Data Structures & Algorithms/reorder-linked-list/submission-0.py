# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        list2 = slow.next
        slow.next = None

        curr = list2
        prev = None
        while curr:
            nextNode = curr.next

            curr.next = prev

            prev = curr

            curr = nextNode

        list1 = head
        list2 = prev

        while list2:
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2

        


        