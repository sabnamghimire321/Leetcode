class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1
     
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch in '+-':
                result += sign * number
                number = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
     
        return result + sign * number
