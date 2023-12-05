class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = 0
        
        for word in words:
            if len(word) > max_len:
                max_len = len(word)
        
        ans = ["" for i in range(max_len)]
        
        for i in range(len(words)):
            for j in range(max_len):
                if len(words[i]) > j:
                    ans[j] += words[i][j]
                else:
                    ans[j] += " "
        res = [a.rstrip() for a in ans]
        return res
        
        