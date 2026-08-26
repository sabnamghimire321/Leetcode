import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = None
        current = self.head
        i = 1
        
        while current:
            if random.randint(1, i) == i:
                result = current.val
            current = current.next
            i += 1
            
        return result
