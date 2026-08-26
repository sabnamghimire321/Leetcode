class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:

            h = min(height[left], height[right])

            area = (right - left) * h

            best = max(best, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best