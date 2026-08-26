class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for x in nums:
            if x in seen:
                return True
            seen.add(x)

        return False