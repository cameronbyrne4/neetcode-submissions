class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = prices[0]
        for p in prices[1:]:
            if p < l:
                l = p   # reset the starting point
            else:
                res = max(res, p - l)

        return res