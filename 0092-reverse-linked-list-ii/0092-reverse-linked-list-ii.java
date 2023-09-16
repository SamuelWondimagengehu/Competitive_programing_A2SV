/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head == null) return null;

        ListNode prev = null;
        ListNode current_node = head;    

        while(left > 1) {
            prev = current_node;
            current_node = current_node.next;
            left--;
            right--;
        }

        ListNode con = prev;
        ListNode tail = current_node;

        while(right > 0) {
            ListNode next = current_node.next;
            current_node.next = prev;
            prev = current_node;
            current_node = next;
            right--;
        }

        if(con != null) {
            con.next = prev;
        } else {
            head = prev;
        }

        tail.next = current_node;
        return head;
    }
}