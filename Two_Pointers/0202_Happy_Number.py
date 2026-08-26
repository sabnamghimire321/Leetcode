class Solution:
    def isHappy(self, n: int) -> bool:
        def next_value(x):
            return sum(int(d) ** 2 for d in str(x))

        slow = n
        fast = next_value(n)

        while fast != 1 and slow != fast:
            slow = next_value(slow)
            fast = next_value(next_value(fast))

        return fast == 1
