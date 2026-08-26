class Solution:

    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        result = []

        def backtrack(index, expr, total, last_operand):
            if index == n:
                if total == target:
                    result.append(expr)
                return
            for end in range(index + 1, n + 1):
                piece = num[index:end]
                if len(piece) > 1 and piece[0] == "0":
                    break
                value = int(piece)
                if index == 0:
                    backtrack(end, piece, value, value)
                else:
                    backtrack(end, expr + "+" + piece, total + value, value)
                    backtrack(end, expr + "-" + piece, total - value, -value)
                    backtrack(
                        end,
                        expr + "*" + piece,
                        total - last_operand + last_operand * value,
                        last_operand * value,
                    )

        backtrack(0, "", 0, 0)
        return result
