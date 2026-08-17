class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minCount = 99999999
        left = 0
        sum = 0
        count = 0
        for right in range(len(nums)):
            sum += nums[right]
            count += 1
            while sum >= target:
                minCount = min(count, minCount)
                sum -= nums[left]
                left += 1
                count -= 1

        if minCount == 99999999:
            return 0
        else:
            return minCount
