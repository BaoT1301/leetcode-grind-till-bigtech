class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        stack = []

        for paren in s:
            if paren not in hash:
                stack.append(paren)
            else:
                if stack and stack[-1] == hash[paren]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False