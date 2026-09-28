class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1

        for key, freq in hash.items():
            if freq > len(nums) // 3:
                res.append(key)

        return res
        
