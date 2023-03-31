class Solution {
    public int pivotIndex(int[] nums) {
        int t_sum = 0;
        for(int i = 0; i < nums.length; i++) {
            t_sum += nums[i];
        }
        
        int left = 0;
        for(int i = 0; i < nums.length; i++) {
            t_sum -= nums[i];
            if(t_sum==left) return i;
            left += nums[i];
        }
        return -1;
    }
}