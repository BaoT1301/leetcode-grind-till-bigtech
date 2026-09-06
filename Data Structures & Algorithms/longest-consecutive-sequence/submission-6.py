class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        length = 0
        maxLength = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if i > 0 and nums[i] == nums[i - 1] + 1:
                length += 1
                maxLength = max(maxLength, length)

            else:
                length = 0

        return maxLength + 1
