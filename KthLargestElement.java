class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        PriorityQueue<String> maxHeap = new PriorityQueue<>((a,b) -> 
            (a.length() != b.length() ? b.length() - a.length() : b.compareTo(a))
        );

        for (String num : nums) {
                maxHeap.offer(num);
        }

        while (k-- > 1) {
            maxHeap.poll();
        }
 
        return maxHeap.peek();  
    }
}
