class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        book = {}
        for i, box in enumerate(boxes):
            if box in book:
                book[box].append(i)
            else:
                book[box] = [i]
                
        if "1" not in book.keys():
            return [0] * len(boxes)
        
        min_nums = []
        for ind, box in enumerate(boxes):
            min_nums.append(sum([abs(val - ind) for val in book["1"]]))
        
        return min_nums