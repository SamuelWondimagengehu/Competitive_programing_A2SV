# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, n: Optional[ListNode])-> ListNode:
        prev = None
        current_node = n
        
        while current_node != None:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
            
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return True
        
        slow = head
        fast = head
        h1 = head
        
        prev = None
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = None
        l = self.reverse(slow)
         
        while h1 != None:
            if h1.val != l.val:
                return False
            h1 = h1.next
            l = l.next
            
        return True
        