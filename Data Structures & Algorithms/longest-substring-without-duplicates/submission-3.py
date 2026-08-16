class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        currLength = 0

        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                currLength -= 1

            seen.add(s[right])
            currLength += 1
            longest = max(longest, currLength)

        return longest