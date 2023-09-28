# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy, length = head, 1
        while dummy.next:
            dummy = dummy.next
            length += 1
        
        dummy.next = head
        k = k % length
        k = length - k
        
        while k > 0:
            dummy = dummy.next            
            k -= 1
        
        head = dummy.next
        dummy.next = None
        
        return head
            
        