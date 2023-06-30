class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        a = 0
        b = len(people) - 1
        remain, n = 0, 0
        
        while a <= b:
            remain = limit - people[b]
            n += 1
            b -= 1
            
            
            if a <= b and remain >= people[a]:
                a += 1
                
        return n
                
        