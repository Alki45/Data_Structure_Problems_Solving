# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        current=dummy

        while head and head.next:
            first_node=head
            second_node=head.next

            current.next=second_node
            first_node.next=second_node.next
            second_node.next=first_node

            current=first_node
            head=first_node.next
        return dummy.next

        