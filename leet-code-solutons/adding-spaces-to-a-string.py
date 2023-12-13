class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        last_index = 0
        
        for space in spaces:
            answer += s[last_index:space]
            last_index = space
            answer += " "
            
        answer += s[last_index:]
        return answer