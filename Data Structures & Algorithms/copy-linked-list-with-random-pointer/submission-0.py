"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoCopy = {None: None}

        curr = head

        while curr:
            newNode = Node(curr.val)
            oldtoCopy[curr] = newNode
            curr = curr.next

        curr = head

        while curr:
            copiedNode = oldtoCopy[curr]
            copiedNode.next = oldtoCopy[curr.next]
            copiedNode.random = oldtoCopy[curr.random]
            curr = curr.next

        return oldtoCopy[head]