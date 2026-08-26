class Solution:

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        used = [False] * len(nums)

        def backtrack(bucket_index, current_sum, start):
            if bucket_index == k:
                return True
            if current_sum == target:
                return backtrack(bucket_index + 1, 0, 0)
            for i in range(start, len(nums)):
                if used[i] or current_sum + nums[i] > target:
                    continue
                if i > start and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                if backtrack(bucket_index, current_sum + nums[i], i + 1):
                    return True
                used[i] = False

            return False

        return backtrack(0, 0, 0)
