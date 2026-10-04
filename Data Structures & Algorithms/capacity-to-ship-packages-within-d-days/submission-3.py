class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        maxWeight = 9999999999

        while left <= right:
            mid = (left + right) // 2
            day = 1
            dayWeight = 0
            for weight in weights:
                dayWeight += weight
                if dayWeight > mid:
                    dayWeight = weight
                    day += 1
                    
            if day <= days:
                maxWeight = min(maxWeight, mid)
                right = mid - 1
            else:
                left = mid + 1

        return maxWeight
                