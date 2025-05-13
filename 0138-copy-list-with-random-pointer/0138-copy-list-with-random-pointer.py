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
        if not head:
                return None

        current = head
        while current:
                new_node = Node(current.val, current.next)
                current.next = new_node
                current = new_node.next
        current = head
        while current:
                if current.random:
                    current.next.random = current.random.next
                current = current.next.next

        dummy_head = Node(0)
        copy = dummy_head
        current = head
        while current:
                next_orig = current.next.next

                copy.next = current.next
                copy = copy.next

                current.next = next_orig
                current = next_orig

        return dummy_head.next