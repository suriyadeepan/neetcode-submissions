class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low and sell high
        lowest = prices[0]
        max_profit = 0
        for p in prices:
            if p < lowest:
                lowest = p
            max_profit = max(max_profit, p - lowest)

        return max_profit