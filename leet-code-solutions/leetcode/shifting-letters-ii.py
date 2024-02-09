class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = list(map(ord, list(s)))
        prefix_nums = [0] * (n + 1)
        
        for shift in shifts:
            l, r, direction = shift[0], shift[1], shift[2]
            
            if direction:
                prefix_nums[l] += 1
                prefix_nums[r + 1] -= 1
            else:
                prefix_nums[l] -= 1
                prefix_nums[r + 1] += 1
                
        for i in range(1, len(prefix_nums)):
            prefix_nums[i] += prefix_nums[i - 1]
        
        for i, val in enumerate(arr):
            arr[i] = ((arr[i] + prefix_nums[i]) - 97) % 26 + 97 
            arr[i] = chr(arr[i])

        return "".join(arr)
            