class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #compare two consecutive words
        #if the index of their characters in order is not proper return false
        #continue until the shortest string ends
        book = {}
        for i, o in enumerate(order):
            book[o] = i
       
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                
                if words[i][j] != words[i + 1][j]:
                    if book[words[i][j]] > book[words[i + 1][j]]:
                        return False
                    break
        return True
                