class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        
        while 1:
            if n % 2 == 0:
                return n
            n += n
            
        