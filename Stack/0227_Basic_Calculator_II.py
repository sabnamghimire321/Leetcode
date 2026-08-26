class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        sign = '+'
        s = s + '+'
     
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch != ' ':
                if sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-number)
                elif sign == '*':
                    stack.append(stack.pop() * number)
                elif sign == '/':
                    stack.append(int(stack.pop() / number))
                sign = ch
                number = 0
     
        return sum(stack)
