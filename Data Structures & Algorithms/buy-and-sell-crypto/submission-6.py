class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left = 0
        right = 1
        for i in range(len(prices)):
            while right< len(prices):
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)

                if prices[left] > prices[right]:
                    left = right
                
                right += 1

        return maxP
