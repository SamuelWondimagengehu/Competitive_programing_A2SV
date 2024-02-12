# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#   self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        current_node, prev = head, None
        
        while left > 1:
            prev, current_node = current_node, current_node.next
            left, right = left - 1, right - 1
        
        con, tail = prev, current_node
        
        while right > 0:
            next_node, current_node.next = current_node.next, prev
            prev, current_node = current_node, next_node
            right -= 1
        
        if con is not None:
            con.next = prev
        else:
            head = prev
        tail.next = current_node
        
        return head
        