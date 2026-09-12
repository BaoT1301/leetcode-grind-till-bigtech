class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for bracket in s:
            if bracket not in hash:
                stack.append(bracket)
            elif stack and stack[-1] == hash[bracket]:
                stack.pop()
            else:
                return False

        return True if not stack else False