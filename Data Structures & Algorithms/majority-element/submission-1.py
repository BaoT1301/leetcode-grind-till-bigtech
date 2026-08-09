class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        sorted_hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)

        return sorted_hash[0][0]