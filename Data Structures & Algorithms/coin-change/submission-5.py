class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # Given 10 coins btw
        coins.sort()
        n = len(coins)

        # O(t) space means we have an array the size of the amount!
        # At each space in that array is the minimum coins to get there!
        # We find that by...

        dp = [1e9] * (amount+1) # +1 to make space for 0 at the start
        dp[0] = 0
        
        '''
        My inner loop shouldve been thru the values of coins
        * We shouldn't calc the # of coins needed as the sum of the amount
            needed to reach two factor
        * We SHOULD calc the # of coins as +1 from the steps where you can one shot the current amt
        '''
        # For each possible amount we want to set the minimum number of coins to get there
        for i in range(1, amount+1):
            # Each amount we should compare the sum of it's minis
            for c in coins: # only have to do half but who cares
                if 0 <= i-c <= amount:
                    dp[i] = min(dp[i], 1+dp[i-c])

        # return
        if dp[-1] != 1e9:
            return dp[-1]
        else:
            return -1