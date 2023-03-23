class Solution {
    public int[] rearrangeArray(int[] nums) {
        Arrays.sort(nums);
        
        int a_ptr = 0;
        int b_ptr = nums.length-1;
        
        int[] answer = new int[nums.length];
        int k = 0;
        
        while(k < nums.length) {
            answer[k] = nums[b_ptr--];
            k += 2;
        }
        
        k = 1;
        
        while(k < nums.length) {
            answer[k] = nums[a_ptr++];
            k += 2;
        }
        
        return answer;
    }
}
