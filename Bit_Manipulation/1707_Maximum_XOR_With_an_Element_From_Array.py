class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        indexed_queries = sorted(range(len(queries)), key=lambda i: queries[i][1])
        result = [-1] * len(queries)
        root = {}
        BITS = 30
        i = 0
     
        def insert(num):
            node = root
            for b in range(BITS, -1, -1):
                bit = (num >> b) & 1
                node = node.setdefault(bit, {})
     
        def query_best(x):
            node = root
            best = 0
            for b in range(BITS, -1, -1):
                bit = (x >> b) & 1
                toggled = 1 - bit
                if toggled in node:
                    best |= (1 << b)
                    node = node[toggled]
                else:
                    if bit not in node:
                        return -1
                    node = node[bit]
            return best
     
        for qi in indexed_queries:
            x, m = queries[qi]
            while i < len(nums) and nums[i] <= m:
                insert(nums[i])
                i += 1
            if root:
                result[qi] = query_best(x)
     
        return result
