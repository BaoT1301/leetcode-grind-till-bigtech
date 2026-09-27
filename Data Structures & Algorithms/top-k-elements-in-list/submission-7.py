class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1

        sorted_seen = sorted(seen.items(), key=lambda x : x[1], reverse=True)

        for key, val in sorted_seen[:k]:
            res.append(key)

        return res