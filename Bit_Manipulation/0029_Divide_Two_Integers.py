class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
     
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while (temp << 1) <= dividend:
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
     
        result = (0 - quotient) if is_negative else quotient
        
        INT_MIN = -(1 << 31)
        INT_MAX = (1 << 31) - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result
