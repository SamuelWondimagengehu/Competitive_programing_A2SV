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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current_node = dummy;

        int carry = 0;
        while(l1 != null || l2 != null) {
            int a = (l1 != null) ? l1.val : 0;
            int b = (l2 != null) ? l2.val : 0;

            int result = a + b + carry;
            carry = result / 10;
            int last_digit = result % 10;

            ListNode node = new ListNode(last_digit);
            current_node.next = node;

            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;

            current_node = current_node.next;
        }

        if(carry > 0) {
            ListNode node = new ListNode(carry);
            current_node.next = node;
        }

        return dummy.next;
    }
}
