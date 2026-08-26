class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                hi = mid - 1
            else:
                lo = mid + 1
