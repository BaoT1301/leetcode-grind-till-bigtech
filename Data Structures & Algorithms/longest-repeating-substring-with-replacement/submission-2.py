class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = {}
        longest = 0
        for right in range(len(s)):
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
            
            max_freq = max(seen.values())
            window_length = right - left + 1

            while window_length - max_freq > k:
                seen[s[left]] -= 1
                left += 1
                window_length -= 1
                max_freq = max(seen.values())

            longest = max(longest, right - left + 1)

        return longest

            


