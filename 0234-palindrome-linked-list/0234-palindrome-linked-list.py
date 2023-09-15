# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a_ptr = head
        b_ptr = head
        arr = []
        
        while a_ptr != None:
            arr.append(a_ptr.val)
            a_ptr = a_ptr.next
        a_ptr, b_ptr = 0, len(arr) - 1
        
        while a_ptr <= b_ptr:
            if arr[a_ptr] != arr[b_ptr]:
                return False
            a_ptr += 1
            b_ptr -= 1
        return True