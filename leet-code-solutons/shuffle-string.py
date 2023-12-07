class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ["x" for i in range(len(s))]
        
        for i, ii in enumerate(indices):
            ans[ii] = s[i]
        return "".join(ans)