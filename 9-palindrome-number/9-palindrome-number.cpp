class Solution {
public:
    bool isPalindrome(int x) {
        std::string str = std::to_string(x); 
        int a_ptr = 0, b_ptr = str.size()-1;
        
        while(a_ptr < b_ptr) {
            if(str[a_ptr] != str[b_ptr]) return false;
            a_ptr++;
            b_ptr--;
        }
        
        return true;
    }
};