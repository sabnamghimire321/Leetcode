class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            sentences = []
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece in words:
                    for rest in backtrack(end):
                        sentences.append(
                            piece + ("" if not rest else " " + rest)
                        )
            memo[start] = sentences
            return sentences

        return backtrack(0)
