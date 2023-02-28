class Solution {
    public void moveZeroes(int[] nums) {
        int a = 0, b = 0;

        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 0) {
                a++;
            } else {
                int temp = nums[a];
                nums[a] = nums[b];
                nums[b] = temp;
                b++;
                a++;
            }
        }
        
    }
}
 
