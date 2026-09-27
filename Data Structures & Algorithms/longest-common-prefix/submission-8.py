class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)

        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
        