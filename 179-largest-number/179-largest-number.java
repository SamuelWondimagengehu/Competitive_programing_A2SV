class Solution {
    public String largestNumber(int[] nums) {
        if(nums.length == 0 || nums == null) return "";
        
        String[] array = new String[nums.length];
        
        for(int i = 0; i < nums.length; i++) {
            array[i] = String.valueOf(nums[i]);
        }
        
        Arrays.sort(array,(s1,s2)->(s2+s1).compareTo(s1+s2));
        
        if(array[0].charAt(0) == '0') return "0";
    
        StringBuilder sb = new StringBuilder();
        
        for(String str : array) {
            sb.append(str);
        }
        
        return sb.toString();
    }
}