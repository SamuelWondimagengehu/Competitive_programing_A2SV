# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        current_node = temp
        
        while list1 and list2:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next
            
        while list1:
            current_node.next = list1
            current_node, list1 = current_node.next, list1.next
            
        while list2:
            current_node.next = list2
            current_node, list2 = current_node.next, list2.next
            
        return temp.next