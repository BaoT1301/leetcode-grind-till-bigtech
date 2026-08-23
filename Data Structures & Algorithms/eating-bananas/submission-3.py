import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left  = 1
        right = max(piles)
        minTotal = 999999999999

        while left <= right:
            speed = (left + right) // 2
            total = 0
            for pile in piles:
                hour = math.ceil(pile / speed)
                total += hour
            
            if total <= h:
                minTotal = min(minTotal, speed)
                right = speed - 1
            else:
                left = speed + 1

        return minTotal
