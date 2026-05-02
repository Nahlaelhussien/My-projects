class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        radius = 0
        
        for house in houses:
            i = bisect_left(heaters, house)
            
            left_dist = float('inf') if i == 0 else house - heaters[i - 1]
           
            right_dist = float('inf') if i == len(heaters) else heaters[i] - house
            
            closest = min(left_dist, right_dist)
            
            radius = max(radius, closest)
        
        return radius
