class Solution: 
    def select(self, arr, i):
        _min = arr[i]
        min_idx = i
        
        for j in range(i, len(arr)):
            if _min > arr[j]:
                min_idx = j
                _min = arr[j]
        
        return min_idx
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            rp = self.select(arr, i)
            arr[rp], arr[i] = arr[i], arr[rp]
