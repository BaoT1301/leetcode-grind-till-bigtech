class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            weight = (left + right) // 2
            day = 0
            count = 1
            for w in weights:
                day += w
                if day > weight:
                    count += 1
                    day = w
            
            if count > days:
                left = weight + 1
            else:
                right = weight - 1

        return left

