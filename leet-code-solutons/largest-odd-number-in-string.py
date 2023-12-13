class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        
        for i in range(len(num) - 1, -1, -1):
            if len(ans) == 0 and int(num[i]) % 2 != 0:
                ans += num[i]
            elif len(ans) >= 1 and int(num[i]) % 2 == 0:
                ans += num[i]
            elif int(num[i]) % 2 != 0:
                ans += num[i]   
            else:
                continue
                
        return ans[::-1]
        