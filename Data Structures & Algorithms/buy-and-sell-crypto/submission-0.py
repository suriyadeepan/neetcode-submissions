class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            profit = p - lowest
            max_profit = max(max_profit, profit)
        return max_profit