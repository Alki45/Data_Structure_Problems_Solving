class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                top = stack.pop()
                if top == '(':
                    stack.append(1)
                else:
                    score = top
                    while stack and stack[-1] != '(':
                        score += stack.pop()
                    stack.pop()
                    stack.append(2 * score)
        return sum(stack)