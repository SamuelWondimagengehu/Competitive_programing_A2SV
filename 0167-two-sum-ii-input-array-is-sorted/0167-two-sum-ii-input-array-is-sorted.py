class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        
        while i <= j:
            curr_sum = numbers[i] + numbers[j]
            if target < curr_sum:
                j -= 1
            elif target > curr_sum:
                i += 1
            else:
                return [i + 1, j + 1]
            
        return []