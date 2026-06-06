class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left = 0
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)

            if prices[left] > prices[right]:
                left = right
            else:
                right += 1

        return maxP
