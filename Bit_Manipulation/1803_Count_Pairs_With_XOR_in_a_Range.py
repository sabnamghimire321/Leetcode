class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        def count_at_most(bound):
            if bound < 0:
                return 0
            root = {}
            BITS = 15 
    
            def insert(num):
                node = root
                for b in range(BITS, -1, -1):
                    bit = (num >> b) & 1
                    node = node.setdefault(bit, {'count': 0})
                    node['count'] += 1
    
            def count_with(num):
                node = root
                total = 0
                for b in range(BITS, -1, -1):
                    if not node:
                        break
                    num_bit = (num >> b) & 1
                    bound_bit = (bound >> b) & 1
                    
                    if bound_bit == 1:
                        same = node.get(num_bit)
                        if same:
                            total += same['count']
                        node = node.get(1 - num_bit)
                    else:
                        node = node.get(num_bit)
                
                if node:
                    total += node['count']
                return total
    
            total = 0
            for num in nums:
                total += count_with(num)
                insert(num)
            return total
    
        return count_at_most(high) - count_at_most(low - 1)
