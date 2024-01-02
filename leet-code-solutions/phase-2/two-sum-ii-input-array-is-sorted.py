class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        sum_ = 0
        
        while numbers[i] + numbers[j] != target:
            sum_ = numbers[i] + numbers[j]
            if sum_ - target > 0:
                j -= 1
            else:
                i += 1
        
        return [i + 1, j + 1]