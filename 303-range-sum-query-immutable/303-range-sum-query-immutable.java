class NumArray {
    int[] n;
    
    public NumArray(int[] nums) {
        n = new int[nums.length];
        
        for(int i = 0; i < n.length; i++) {
            n[i] = nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        int sum = 0;
        while(left<=right) {
            sum += n[left];
            left++;
        }
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */