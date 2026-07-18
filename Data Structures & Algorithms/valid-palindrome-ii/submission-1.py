class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1

            return True
        

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                if isPalindrome(left + 1, right):
                    return True
                if isPalindrome(left, right - 1):
                    return True

                return False

            left += 1
            right -= 1

        return True