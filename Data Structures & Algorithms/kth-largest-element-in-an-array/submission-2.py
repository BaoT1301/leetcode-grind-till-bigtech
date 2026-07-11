class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]

        maxHeap = nums
        heapq.heapify(maxHeap)

        while k > 0:
            val = -heapq.heappop(maxHeap)
            k -=1

        return val