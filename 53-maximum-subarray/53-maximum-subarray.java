class Solution {
    public int maxSubArray(int[] nums) {
        int lm = nums[0];
        int gm = nums[0];
        
        for(int i = 1; i < nums.length; i++) {
            lm = Math.max(nums[i],nums[i]+lm);
            if(lm>gm) gm = lm;
        }
        
        return gm;
    }
}