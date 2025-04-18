# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=0
        current=head
        while current:
            length+=1
            current=current.next
            
        
        
        size=length//k
        remainder=length%k
        arr=[]

        new_node=head

        for i in range(k):
            new_head=new_node
            new=[]
            if(i<remainder):
                current_size=size +1
            else:
                current_size=size
            for _ in range(current_size-1):
                if new_node:
                    new_node=new_node.next
            if new_node:
                next_part = new_node.next
                new_node.next = None
                new_node = next_part
            arr.append(new_head)
        return arr
        