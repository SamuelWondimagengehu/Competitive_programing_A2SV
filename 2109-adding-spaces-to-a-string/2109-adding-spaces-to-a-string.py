class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        last_index = 0
        
        for space in spaces:
            ans += s[last_index:space]
            last_index = space
            ans += ' '
        ans += s[last_index:]
        
        return ans