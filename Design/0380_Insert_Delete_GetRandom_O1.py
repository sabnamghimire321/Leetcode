import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index_of = {}

    def insert(self, val: int) -> bool:
        if val in self.index_of:
            return False
        self.index_of[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_of:
            return False
        idx = self.index_of[val]
        last_val = self.values[-1]
        self.values[idx] = last_val
        self.index_of[last_val] = idx
        self.values.pop()
        del self.index_of[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
