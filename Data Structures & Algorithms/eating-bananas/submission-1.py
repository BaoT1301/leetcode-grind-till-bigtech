class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            totalHours = 0
            for pile in piles:
                hour = math.ceil(pile / mid)
                totalHours += hour
            
            if totalHours > h:
                left = mid + 1
            else:
                right = mid - 1

        return left