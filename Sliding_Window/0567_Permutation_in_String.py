from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
            
        target = Counter(s1)
        window = Counter()
        matches = 0
        
        for i in range(m):
            window[s2[i]] += 1
            
        for char in target:
            if window[char] == target[char]:
                matches += 1
                
        if matches == len(target):
            return True
            
        for i in range(m, n):
            r_char = s2[i]
            if r_char in target:
                if window[r_char] == target[r_char]:
                    matches -= 1
                window[r_char] += 1
                if window[r_char] == target[r_char]:
                    matches += 1
                    
            l_char = s2[i - m]
            if l_char in target:
                if window[l_char] == target[l_char]:
                    matches -= 1
                window[l_char] -= 1
                if window[l_char] == target[l_char]:
                    matches += 1
                    
            if matches == len(target):
                return True
                
        return False
