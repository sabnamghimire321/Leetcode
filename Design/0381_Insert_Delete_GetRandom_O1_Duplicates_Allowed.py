import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.values = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        is_new = not self.indices[val]
        self.indices[val].add(len(self.values))
        self.values.append(val)
        return is_new

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        
        remove_idx = self.indices[val].pop()
        last_val = self.values[-1]
        last_idx = len(self.values) - 1

        self.values[remove_idx] = last_val
        if last_idx != remove_idx:
            self.indices[last_val].discard(last_idx)
            self.indices[last_val].add(remove_idx)

        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
