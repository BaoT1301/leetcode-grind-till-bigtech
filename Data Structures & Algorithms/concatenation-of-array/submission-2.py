class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(2):
            for k in range(len(nums)):
                res.append(nums[k])

        return res