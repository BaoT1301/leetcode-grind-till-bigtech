class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        answer = []
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1

        for key, val in seen.items():
            res.append((val, key))
        
        heapq.heapify(res)

        while len(res) > k:
            heapq.heappop(res)

        for key, val in res:
            answer.append(val)

        return answer