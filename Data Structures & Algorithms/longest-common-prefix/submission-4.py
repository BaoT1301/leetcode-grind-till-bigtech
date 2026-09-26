class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        res = ""

        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return res
            res += word[i]
                
        return res