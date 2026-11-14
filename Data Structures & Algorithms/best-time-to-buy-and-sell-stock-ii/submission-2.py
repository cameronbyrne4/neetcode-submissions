class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Same as buy and sell but we add to a total with every sell
        # If more, we sell
        # If less, we reset buy price (sold the previous day for same price we bought it at, so we can buy the cheaper one on today)
        total = 0
        buy = prices[0] # index that we bought at

        for p in prices[1:]:
            if p > buy:
                total += (p-buy)
            buy = p

        return total