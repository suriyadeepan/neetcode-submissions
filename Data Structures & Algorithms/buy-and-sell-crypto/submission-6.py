class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while l < r and r < len(prices):
            # calculate profit
            profit = prices[r] - prices[l]
            # update maxProfit
            maxProfit = max(profit, maxProfit)
            # bad deal?
            if profit <= 0:
                l = r
            # move right pointer
            r += 1

        return maxProfit
                