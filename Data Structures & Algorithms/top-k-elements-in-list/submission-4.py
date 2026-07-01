class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        answer = []
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        sorted_num = sorted(hash.items(), key=lambda x: x[1], reverse=True)

        for num, freq in sorted_num[:k]:
            answer.append(num)

        return answer


        