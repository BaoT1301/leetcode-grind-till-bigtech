class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxHeight = 0
        for i in range(len(heights)):
            area = right - left
            height = min(heights[left], heights[right])
            areaHeight = area * height
            maxHeight = max(maxHeight, areaHeight)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxHeight
