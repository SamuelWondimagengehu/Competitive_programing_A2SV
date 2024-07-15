impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        if n == 1 {
            return true
        } else if n < 1 || n % 3 != 0 {
            return false
        }
        
        Self::is_power_of_three(n / 3)
    }
}