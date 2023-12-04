class Solution:
    def romanToInt(self, s: str) -> int:
        book = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        ans = []
        for c in s:
            if len(ans) and book[c] > ans[-1]:
                ans.append(book[c] - ans.pop())
            else:
                ans.append(book[c])
        return sum(ans)
            
                