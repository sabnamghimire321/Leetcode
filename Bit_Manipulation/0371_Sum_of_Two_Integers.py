class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry & mask
            
        a = a & mask
        
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
