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

        
        slow2 = slow.next
        slow.next = None

        prev = None
        curr = slow2
        while curr:
            nextNode = curr.next

            curr.next = prev

            prev = curr

            curr = nextNode

        while prev and head:
            next1 = head.next
            prev2 = prev.next

            head.next = prev
            prev.next = next1

            head = next1
            prev = prev2


        