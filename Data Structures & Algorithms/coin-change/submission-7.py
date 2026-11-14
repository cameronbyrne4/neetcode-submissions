class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0 # not sure abt this one

        for c in coins:
            if c <= amount:
                dp[c] = 1   # obviously min is one coin
        
        for i in range(1,amount+1):
            # Update dp to min of all the decremented coins + 1
            
            for c in coins:
                # Must be in range:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
            
        



        return dp[amount] if dp[amount] != float('inf') else -1