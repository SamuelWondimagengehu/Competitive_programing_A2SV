class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = set()
        ugly_nums.add(1)
        
        ugly_num = 1
        for i in range(n):
            ugly_num = min(ugly_nums)
            
            ugly_nums.remove(ugly_num)
            
            ugly_nums.add(ugly_num * 2)
            ugly_nums.add(ugly_num * 3)
            ugly_nums.add(ugly_num * 5)
                
        return ugly_num