class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                x, y = stack[-1], stack[-2]
                stack.append(x + y)
            elif op == "D":
                x = stack[-1]
                stack.append(2 * x)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)