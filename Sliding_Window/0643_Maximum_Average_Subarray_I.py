class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            best = max(best, window_sum)

        return best / k
