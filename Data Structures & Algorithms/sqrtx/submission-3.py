class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        best = 0

        while left <= right:
            mid = (left + right) // 2
            root = mid * mid

            if root <= x:
                best = max(best, mid)
                left = mid + 1
            elif root > x:
                right = mid - 1

        return best