class Bucket:
    def __init__(self, count: int):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_bucket = {}   
        self.head = Bucket(0)    
        self.tail = Bucket(0)    
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, node: Bucket, count: int) -> Bucket:
        bucket = Bucket(count)
        bucket.prev, bucket.next = node, node.next
        node.next.prev = bucket
        node.next = bucket
        self.count_bucket[count] = bucket
        return bucket

    def _remove(self, bucket: Bucket) -> None:
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev
        del self.count_bucket[bucket.count]

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        self.key_count[key] = count + 1
        new_bucket = self.count_bucket.get(count + 1) or self._insert_after(
            self.count_bucket.get(count, self.head), count + 1)
        new_bucket.keys.add(key)
        if count > 0:
            old_bucket = self.count_bucket[count]
            old_bucket.keys.remove(key)
            if not old_bucket.keys:
                self._remove(old_bucket)

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        old_bucket = self.count_bucket[count]
        old_bucket.keys.remove(key)
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] = count - 1
            new_bucket = self.count_bucket.get(count - 1) or self._insert_after(
                old_bucket.prev, count - 1)
            new_bucket.keys.add(key)
        if not old_bucket.keys:
            self._remove(old_bucket)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev is not self.head else ''

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next is not self.tail else ''
