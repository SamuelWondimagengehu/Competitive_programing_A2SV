class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = 0
        
        # get the length of the longest string in the array
        for word in words:
            if len(word) > max_len:
                max_len = len(word)
                
        # initialize the answer array with empty strings
        ans = ["" for i in range(max_len)]
        
        for i in range(len(words)):
            for j in range(max_len):
                if len(words[i]) > j:
                    ans[j] += words[i][j] # append the jth substring of every string in words
                else:
                    ans[j] += " "
        
        ans = [word.rstrip() for word in ans] # remove trailing spaces from every string in ans
        return ans
        
        