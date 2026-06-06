class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0

        left = 0
        for right in range(len(s)):
                if s[right] not in seen:
                    seen.add(s[right])
                else:
                    while s[right] in seen:
                        seen.remove(s[left])
                        left += 1
                seen.add(s[right])
                
                maxLen = max(maxLen, len(seen))
        
        return maxLen

                
            