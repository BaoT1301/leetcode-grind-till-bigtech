class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        length = 1
        maxLength = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                length += 1
                maxLength = max(length, maxLength)
            elif nums[i] == nums[i + 1]:
                continue
            else:
                length = 1
        return maxLength 