class Solution:
    def topKFrequent(self, nums, k):
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1

        sorted_item = sorted(seen.items(), key=lambda item: item[1], reverse=True)

        res = []

        for num, freq in sorted_item[:k]:
            res.append(num)

        return res
