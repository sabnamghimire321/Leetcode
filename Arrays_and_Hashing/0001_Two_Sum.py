class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, x in enumerate(nums):
            complement = target - x

            if complement in seen:
                return [seen[complement], i]

            seen[x] = i

        return []