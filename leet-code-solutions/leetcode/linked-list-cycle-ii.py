# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        fast, runner = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            runner = runner.next
            if runner == fast:
                break
        
        if fast == None or fast.next == None:
            return None
        
        while head != runner:
            head = head.next
            runner = runner.next
            
        return head