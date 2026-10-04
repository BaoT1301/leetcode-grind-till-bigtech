class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            decoded = ""
            number = ""
            if char == "]":
                while stack[-1] != "[":
                    decoded = stack.pop() + decoded
                stack.pop()
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number

                stack.append(decoded * int(number))
            if char != "]":
                stack.append(char)

        return "".join(stack)