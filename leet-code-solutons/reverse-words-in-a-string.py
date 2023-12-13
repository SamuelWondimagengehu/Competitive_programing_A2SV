class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for word in s.split(" "):
            ans.append(word)
        
        return " ".join([word for word in ans[::-1] if word != ""]).strip()