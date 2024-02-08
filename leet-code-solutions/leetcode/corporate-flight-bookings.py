class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n + 1)

        for i in range(len(bookings)):
            first, last, seats = bookings[i]
            answer[first - 1] += seats
            answer[last] -= seats
        
        for i in range(1, n):
            answer[i] += answer[i - 1]
        
        return answer[:-1]