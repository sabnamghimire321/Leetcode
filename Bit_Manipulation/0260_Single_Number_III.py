class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        combined_xor = 0
        for x in nums:
            combined_xor ^= x
     
        diff_bit = combined_xor & (-combined_xor)
     
        a = 0
        for x in nums:
            if x & diff_bit:
                a ^= x
        b = combined_xor ^ a
     
        return [a, b]
