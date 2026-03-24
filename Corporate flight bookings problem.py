from collections import defaultdict
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dic = defaultdict(int)
        for start, end, seats in bookings:
            dic[start - 1] += seats
            dic[end] -= seats
        arr=[0]*n
        running_sum=0
        for i in range(n):
            running_sum+=dic[i]
            arr[i]=running_sum
        return arr

