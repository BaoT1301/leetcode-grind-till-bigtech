import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            totalhours = 0

            for pile in piles:
                hours = math.ceil(pile / mid)
                totalhours += hours
            if totalhours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
