class Solution {
    public int largestAltitude(int[] gain) {
        int c = 0;
        int a = 0;
        
        for(int i : gain) {
            c += i;
            a = Math.max(c,a);
        }
        
        return a;
    }
}