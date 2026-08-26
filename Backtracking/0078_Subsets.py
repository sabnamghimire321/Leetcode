class Solution:

  def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []
    path = []

    def backtrack(start):
      result.append(list(path))
      for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()

    backtrack(0)
    return result
