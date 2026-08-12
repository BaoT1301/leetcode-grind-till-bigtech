class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxWidth = 0

        while left < right:
            width = right - left
            minHeight = min(heights[left], heights[right])
            width2 = minHeight * width
            maxWidth = max(maxWidth, width2)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        

        return maxWidth

