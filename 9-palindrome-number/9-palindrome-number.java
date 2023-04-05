class Solution {
    public boolean isPalindrome(int x) {
        String str = String.valueOf(x);
        
        int a_ptr = 0, b_ptr = str.length()-1;
        
        while(a_ptr < b_ptr) {
            if(str.charAt(a_ptr) != str.charAt(b_ptr)) return false;
            a_ptr++;
            b_ptr--;
        }
        
        return true;
    }
}