class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}

        left = 0
        length = 0
        for right in range(len(s)):
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
            
            max_element = max(seen.values())

            while (right - left + 1) - max_element > k:
                seen[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)

        return length

            

