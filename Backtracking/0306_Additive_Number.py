class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid_start(s):
            return s == "0" or s[0] != "0"

        def backtrack(first, second, rest):
            if not rest:
                return True
            expected = str(int(first) + int(second))
            if rest.startswith(expected):
                return backtrack(second, expected, rest[len(expected) :])
            return False

        for i in range(1, n):
            if not valid_start(num[:i]):
                break
            for j in range(i + 1, n):
                if not valid_start(num[i:j]):
                    break
                if backtrack(num[:i], num[i:j], num[j:]):
                    return True
        return False
