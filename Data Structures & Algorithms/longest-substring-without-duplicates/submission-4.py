class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        length = 0

        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                length -= 1
            
            seen.add(s[right])
            length += 1
            max_length = max(length, max_length)

        return max_length
