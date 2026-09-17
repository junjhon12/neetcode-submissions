class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                num_two = stack.pop()
                num_one = stack.pop()

                if token == "+":
                    stack.append(num_one + num_two)
                elif token == "-":
                    stack.append(num_one - num_two)
                elif token == "*":
                    stack.append(num_one * num_two)
                elif token == "/":
                    stack.append(int(num_one / num_two))
            else:
                stack.append(int(token))
        return stack[0]

