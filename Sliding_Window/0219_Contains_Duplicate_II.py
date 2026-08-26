class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for i, x in enumerate(nums):
            if x in window:
                return True

            window.add(x)

            if len(window) > k:
                window.remove(nums[i - k])

        return False