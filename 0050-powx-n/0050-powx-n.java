class Solution {
    public double myPow(double x, int n) {
        //x^1101
        long power = Math.abs((long) n);
        double result = 1;
        
        while(power > 0) {
            if((power & 1) == 1)
                result = result * x;
            
            x *= x;               
            power >>= 1;
        }
        
        return n >= 0 ? result : 1 / result;
    }
}