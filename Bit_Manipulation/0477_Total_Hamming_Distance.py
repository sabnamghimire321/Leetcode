class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for bit in range(32):
            c = sum((x >> bit) & 1 for x in nums)
            total += c * (n - c)
        return total
