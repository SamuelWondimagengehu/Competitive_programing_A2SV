class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs = [str(digit) for digit in digits]

        num = int("".join(strs))

        num += 1

        ans = []
        string = str(num)

        for c in string:
            ans.append(int(c))
        
        return ans
        