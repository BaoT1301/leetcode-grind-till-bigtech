# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        prev = None
        curr = second_half

        while curr:
            nextNode = curr.next

            curr.next = prev

            prev = curr

            curr = nextNode

        while head and prev:

            Next1 = head.next
            Next2 = prev.next

            head.next = prev
            prev.next = Next1

            head = Next1
            prev = Next2

