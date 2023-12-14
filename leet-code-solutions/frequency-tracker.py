class FrequencyTracker:
    
    def __init__(self):
        self.freq_num = Counter()
        self.num_freq = Counter()
        
    def add(self, number: int) -> None:
        temp = self.num_freq[number]
        self.num_freq[number] += 1
        self.freq_num[temp] -= 1
        self.freq_num[temp + 1] += 1
        
    def deleteOne(self, number: int) -> None:    
        temp = self.num_freq[number]
        
        if temp == 0:
            return 
        self.num_freq[number] -= 1
        self.freq_num[temp] -= 1
        self.freq_num[temp - 1] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_num[frequency] >= 1
        
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)