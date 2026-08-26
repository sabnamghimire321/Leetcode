class Solution:
    def shortestPalindrome(self, s: str) -> str:
        combined = s + '#' + s[::-1]
        n = len(combined)
        lps = [0] * n
        length = 0
        i = 1
        
        while i < n:
            if combined[i] == combined[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
 
        palindrome_prefix_len = lps[-1]
        to_add = s[palindrome_prefix_len:][::-1]
        return to_add + s
