class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
 
        def is_palindrome(sub):
            return sub == sub[::-1]
 
        def backtrack(start):
            if start == len(s):
                result.append(list(path))
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if is_palindrome(piece):
                    path.append(piece)
                    backtrack(end)
                    path.pop()
 
        backtrack(0)
        return result
