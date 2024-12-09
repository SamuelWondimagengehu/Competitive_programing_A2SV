class Solution {
    public final static int MOD = 1337;
    
    public int superPow(int a, int[] b) {
        int result = 1;
        a %= MOD;
        
        for(int digit : b) {
            result = (pow(result, 10) * pow(a, digit)) % MOD;
        }
        
        return result;
    }
  
    private int pow(int a, int power) {
        int result = 1;
        
        while(power > 0) {
            if((power & 1) == 1)
                result = (result * a) % MOD;
            
            a = (a * a) % MOD; 
            power >>= 1;
        }
        
        return result;
    }
}