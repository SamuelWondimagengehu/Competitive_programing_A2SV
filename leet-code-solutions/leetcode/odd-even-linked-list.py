# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def go_to_end(self,n):
        while n.next:
            n = n.next
        return n
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        odds, evens = ListNode(), ListNode()
        odd, even = None, None
        i = 1
        while dummy:
            if i % 2 == 0:
                even = self.go_to_end(evens)
                even.next = ListNode(dummy.val)
            else:
                odd = self.go_to_end(odds)
                odd.next = ListNode(dummy.val)
            i += 1
            dummy = dummy.next
        odd = self.go_to_end(odds)
        odd.next = evens.next
        return odds.next