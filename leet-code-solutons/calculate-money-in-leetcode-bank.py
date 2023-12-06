class Solution:
    def totalMoney(self, n: int) -> int:
        ans = []
        if n <= 7:
            return sum([i for i in range(1, n + 1)])
        
        rem = n % 7
        n = n - rem
        
        for i in range(1, (n // 7) + 1) :
            if len(ans) > 0:
                ans.append([j for j in range(ans[-1][0] + 1, ans[-1][-1] + 2)])
            else:
                ans.append([j for j in range(1, 8)])
        
        ans.append([i + ans[-1][0] for i in range(1, rem + 1)])

        ans = [sum(deps) for deps in ans]
        return sum(ans)
        
        
            
                