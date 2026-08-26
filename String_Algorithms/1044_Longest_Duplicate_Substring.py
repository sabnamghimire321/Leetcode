class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        BASE, MOD = 26, (1 << 31) - 1

        def search(length):
            h = 0
            for i in range(length):
                h = (h * BASE + nums[i]) % MOD

            seen = {h: [0]}
            power = pow(BASE, length, MOD)

            for start in range(1, n - length + 1):
                h = (h * BASE - nums[start - 1] * power + nums[start + length - 1]) % MOD

                if h in seen:
                    for prev_start in seen[h]:
                        if s[prev_start:prev_start + length] == s[start:start + length]:
                            return start
                    seen[h].append(start)
                else:
                    seen[h] = [start]

            return -1

        lo, hi = 1, n - 1
        result = ''

        while lo <= hi:
            mid = (lo + hi) // 2
            pos = search(mid)

            if pos != -1:
                result = s[pos:pos + mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return result