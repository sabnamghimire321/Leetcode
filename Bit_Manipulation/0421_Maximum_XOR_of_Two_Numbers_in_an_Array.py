class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        BITS = 31
     
        for num in nums:
            node = root
            for i in range(BITS, -1, -1):
                bit = (num >> i) & 1
                node = node.setdefault(bit, {})
     
        best = 0
        for num in nums:
            node = root
            current_xor = 0
            for i in range(BITS, -1, -1):
                bit = (num >> i) & 1
                toggled = 1 - bit
                if toggled in node:
                    current_xor |= (1 << i)
                    node = node[toggled]
                else:
                    node = node[bit]
            best = max(best, current_xor)
     
        return best
