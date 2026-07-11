class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        maxHeap = stones
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)

            if first != second:
                heapq.heappush(maxHeap, -(first - second))
        
        return -maxHeap[0] if maxHeap else 0