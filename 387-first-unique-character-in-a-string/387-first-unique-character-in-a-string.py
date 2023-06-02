class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = Counter(s)
        
        for i, c in enumerate(s):
            if charCount[c] == 1:
                return i
        return -1
        