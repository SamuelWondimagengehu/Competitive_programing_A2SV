class Solution:
    def reverse(self, x: int) -> int:
        if x != 0:
            sign = x // abs(x)
            x = abs(x)
        else:
            sign = 1
        result = 0
        
        while x != 0:
            lsd = x % 10
            result *= 10
            result += lsd
            x //= 10
        
        result = sign * result
        
        if result < -2**31 or result > (2**31-1):
            result = 0
        return result
