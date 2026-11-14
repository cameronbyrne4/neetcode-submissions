class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        for i in range(1,len(prices)):
            daily =  prices[i] - prices[i-1]
            if daily > 0:
                pro += daily

        return pro