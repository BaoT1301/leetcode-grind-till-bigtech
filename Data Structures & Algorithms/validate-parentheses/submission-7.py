class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for char in s:

            if char not in hash:
                stack.append(char)
            else:
                if stack and hash[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False

        