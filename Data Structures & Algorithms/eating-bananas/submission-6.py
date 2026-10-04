class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minSpeed = 999999999999999

        while left <= right:
            speed = (left + right) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / speed)
            if hour <= h:
                minSpeed = min(minSpeed, speed)
                right = speed - 1
            else:
                left = speed + 1

        return minSpeed