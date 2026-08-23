class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x 
        power2 = 0

        while left <= right:
            mid = (left + right) // 2
            power = mid * mid
            
            if power == x:
                return mid
            elif power > x:
                right = mid - 1
            else:
                left = mid + 1
                power2 = max(mid, power2)

        return power2
