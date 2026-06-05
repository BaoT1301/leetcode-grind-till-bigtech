class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        
        sorted_seen = sorted(seen.items(), key = lambda x: x[1], reverse=True)

        res = []
        for num, freq in sorted_seen[:k]:
            res.append(num)

        return res