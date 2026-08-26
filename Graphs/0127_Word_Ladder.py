from collections import deque
import string
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        words.discard(beginWord)

        while queue:
            word, dist = queue.popleft()

            if word == endWord:
                return dist

            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    candidate = word[:i] + ch + word[i+1:]

                    if candidate in words:
                        words.remove(candidate)
                        queue.append((candidate, dist + 1))

        return 0
