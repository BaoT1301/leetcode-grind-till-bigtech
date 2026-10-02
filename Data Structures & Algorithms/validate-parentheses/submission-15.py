class Solution:
    def isValid(self, s: str) -> bool:
        seen = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        stack = []

        for bracket in s:
            if bracket not in seen:
                stack.append(bracket)
            elif stack and stack[-1] == seen[bracket]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False