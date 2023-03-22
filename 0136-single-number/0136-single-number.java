class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        
        Arrays.sort(nums);
        
        for(int i : nums) {
            if(!set.contains(i)) set.add(i);
            else set.remove(i);
        }
        
        Integer[] arr = set.toArray(new Integer[set.size()]);
        
        return arr[0];
    }
}

    