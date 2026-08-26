from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
            
        target = Counter(t)
        required = len(target)
        window = {}
        formed = 0
        
        left = 0
        best_len, best_left = float('inf'), 0
        
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in target and window[ch] == target[ch]:
                formed += 1
                
            while formed == required:
                if right - left + 1 < best_len:
                    best_len, best_left = right - left + 1, left
                
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in target and window[left_ch] < target[left_ch]:
                    formed -= 1
                left += 1
                
        return "" if best_len == float('inf') else s[best_left:best_left + best_len]
