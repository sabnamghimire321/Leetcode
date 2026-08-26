class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = None
        self.has_peeked = False
        

    def peek(self):
        if not self.has_peeked:
            self.peeked = self.iterator.next()
            self.has_peeked = True
        return self.peeked
        

    def next(self):
        if self.has_peeked:
            val = self.peeked
            self.has_peeked = False
            return val
        return self.iterator.next()
        

    def hasNext(self):
        return self.has_peeked or self.iterator.hasNext()
