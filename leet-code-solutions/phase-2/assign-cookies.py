class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        
        answer = 0
        a_ptr, b_ptr = 0, 0
        g.sort()
        s.sort()
        
        while a_ptr < len(g) and b_ptr < len(s):
            if g[a_ptr] <= s[b_ptr]:
                a_ptr += 1
                b_ptr += 1
                answer += 1
            else:
                b_ptr += 1
        
        return answer
        