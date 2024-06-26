class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(a, b):
            if a < b:
                s[a], s[b] = s[b], s[a]
                helper(a + 1, b - 1)
                
        helper(0, len(s) - 1)