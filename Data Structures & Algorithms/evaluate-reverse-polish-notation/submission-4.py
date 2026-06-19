class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif token == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                val = b - a
                stack.append(val)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                val = int(b / a)
                stack.append(val)
            else:
                stack.append(int(token))

        return stack[-1]