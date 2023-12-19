class Solution:
    def minimizedStringLength(self, s: str) -> int:
        hash_set = set(s)
        n = len(s) - len(hash_set)
        return len(s) - n
                
