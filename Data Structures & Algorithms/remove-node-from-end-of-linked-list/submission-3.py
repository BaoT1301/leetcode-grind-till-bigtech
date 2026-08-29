# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        node = length - n
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while node  > 0:
            curr = curr.next
            node -= 1

        curr.next = curr.next.next

        return dummy.next

