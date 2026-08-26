from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        BASE, MOD = 4, 2**32 - 1
     
        h = 0
        power = pow(BASE, 9, MOD)
        for i in range(10):
            h = (h * BASE + mapping[s[i]]) % MOD
     
        seen = {h}
        repeated = set()
        for i in range(10, n):
            h = ((h - mapping[s[i-10]] * power) * BASE + mapping[s[i]]) % MOD  
            if h in seen:
                repeated.add(s[i-9:i+1])
            seen.add(h)
        return list(repeated)
