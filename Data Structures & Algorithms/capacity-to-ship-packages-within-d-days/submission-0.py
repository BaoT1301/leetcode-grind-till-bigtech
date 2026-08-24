class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = ( left + right)  // 2
            sums = 0
            day = 1
            for weight in weights:
                sums += weight

                if sums > mid:
                    day += 1
                    sums = weight
            if day > days:
                left = mid + 1
            else:
                    
                right = mid - 1

        return left