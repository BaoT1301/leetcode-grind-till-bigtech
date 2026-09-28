class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        maxLength = 0
        for i in range(len(nums)):
            seen.add(nums[i])

        for num in seen:
            current = num
            length = 1
            if current - 1 in seen:
                continue
            while current + 1 in seen:
                length += 1
                current += 1
            maxLength = max(maxLength, length)

        return maxLength


