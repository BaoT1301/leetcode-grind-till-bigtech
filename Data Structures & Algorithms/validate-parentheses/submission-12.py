class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for i in range(len(s)):
            if s[i] not in hash:
                stack.append(s[i])
            elif stack and stack[-1] == hash[s[i]]:
                    stack.pop()
            else:
                return False

        return True if not stack else False