class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        major_element = max(hash, key=hash.get)
        return major_element