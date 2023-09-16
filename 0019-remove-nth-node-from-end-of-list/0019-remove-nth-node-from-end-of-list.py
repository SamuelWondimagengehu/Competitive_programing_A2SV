# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = head
        nodes = 0
        while dummy:
            nodes += 1
            dummy = dummy.next
        nodes = nodes - n
        prev = None
        curr = head
        
        if nodes == 0 or nodes == -1:
            return head.next
        
        while nodes > 0:
            prev = curr
            curr = curr.next
            nodes -= 1
        prev.next = curr.next
        
        return head
        