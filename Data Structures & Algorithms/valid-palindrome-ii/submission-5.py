class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def Palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True
        while left < right:
            if s[left] != s[right]:
                if Palindrome(left + 1, right) or Palindrome(left, right-1):
                    return True
                return False

            left += 1
            right -= 1

        return True


        
