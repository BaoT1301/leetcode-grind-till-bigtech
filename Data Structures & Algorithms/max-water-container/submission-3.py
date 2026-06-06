class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_width = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            area = min(heights[left], heights[right])
            water = width * area
            max_width = max(water, max_width)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
            
        return max_width
        
            
            
