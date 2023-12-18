class Solution:
    def squares_sum(self, n):
        output = 0
        
        while n:
            digit = n % 10
            output += digit **2
            n = n // 10
        
        return output
    
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        
        while n not in hash_set:
            hash_set.add(n)
            
            n = self.squares_sum(n)
            
            if n == 1:
                return True
        
        return False