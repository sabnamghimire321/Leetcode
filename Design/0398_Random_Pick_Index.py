import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.positions = {}

        for i, x in enumerate(nums):
            if x not in self.positions:
                self.positions[x] = []

            self.positions[x].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.positions[target])