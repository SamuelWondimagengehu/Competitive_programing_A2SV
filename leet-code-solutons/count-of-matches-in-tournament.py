class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = []
        temp = n
        
        for i in range(n):
            if temp % 2 == 0:
                matches.append(temp // 2)
                temp /= 2
            else:
                matches.append((temp - 1) // 2)
                temp = ((temp - 1) / 2) + 1
        print(matches)
        return int(sum(matches))