class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWidth = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            widthlength = right - left
            minHeight = min(heights[left], heights[right])
            width = widthlength * minHeight
            maxWidth = max(maxWidth, width)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWidth
