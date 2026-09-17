class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        condition = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for symbol in s:
            if symbol in condition:
                if stack and stack[-1] == condition[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        return len(stack) == 0