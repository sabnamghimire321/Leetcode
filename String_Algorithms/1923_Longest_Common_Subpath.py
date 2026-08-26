from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        BASE, MOD = 100005, (1 << 61) - 1
 
        def hashes_of_length(path, length):
            power = pow(BASE, length - 1, MOD)
            h = 0
            for i in range(length):
                h = (h * BASE + path[i]) % MOD
            result = {h}
            for i in range(length, len(path)):
                h = ((h - path[i-length] * power) * BASE + path[i]) % MOD
                result.add(h)
            return result
 
        def has_common_of_length(length):
            common = hashes_of_length(paths[0], length)
            for path in paths[1:]:
                common &= hashes_of_length(path, length)
                if not common:
                    return False
            return bool(common)
 
        lo, hi = 1, min(len(p) for p in paths)
        result = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_common_of_length(mid):
                result = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return result
