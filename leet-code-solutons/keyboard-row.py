class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1, row_2, row_3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        ans = []
        
        for word in words:
            temp = word
            word = word.lower()
            flag = 0
            
            if word[0] in row_1:
                res_row = row_1
            elif word[0] in row_2:
                res_row = row_2
            else:
                res_row = row_3
            
            for i in range(len(word)):
                if word[i] not in res_row:
                    flag = 1
                    break
            
            if flag == 0:
                ans.append(temp)
        
        return ans
            
            
                    