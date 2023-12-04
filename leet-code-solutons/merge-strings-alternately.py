class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        answer = ""
        while a < len(word1) and b < len(word2):
            answer += word1[a] + word2[b]
            a += 1
            b += 1
        
        if len(word1) < len(word2):
            answer += word2[b:]
        if len(word1) > len(word2):
            answer += word1[a:]
        
        return answer