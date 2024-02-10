# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_to_last(self, node):
        while node.next != None:
            node = node.next
        return node
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_node = head
        left = ListNode()
        right = ListNode()
        
        while dummy_node != None:
            n = ListNode(dummy_node.val)
            
            if dummy_node.val < x:
                last = self.get_to_last(left)
                last.next = n
            elif dummy_node.val >= x:
                last = self.get_to_last(right)
                last.next = n
            dummy_node = dummy_node.next
            
        
        left_dummy = left
        while left_dummy.next != None:
            left_dummy = left_dummy.next
        
        left_dummy.next = right.next
    
        return left.next
        