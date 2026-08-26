class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        used = [False] * len(nums)
     
        def backtrack():
            if len(path) == len(nums):
                result.append(list(path))
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue  
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False
     
        backtrack()
        return result
