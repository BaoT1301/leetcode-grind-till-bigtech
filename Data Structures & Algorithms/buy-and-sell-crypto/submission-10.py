class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxP = 0
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
            if prices[left] > prices[right]:
                left = right

        return maxP