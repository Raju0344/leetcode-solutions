class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        max_prof = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            sell = prices[i]
            profit = sell - buy
            max_prof = max(max_prof, profit)

        return max_prof
