class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        res = []

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        sorted_hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)

        for k, v in sorted_hash[:k]:
            res.append(k)

        return res
