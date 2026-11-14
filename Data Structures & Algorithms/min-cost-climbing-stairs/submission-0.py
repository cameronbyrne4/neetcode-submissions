class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        i track the minimum cost to get to each stair.
        At a stair I:
            val = add it's cost + the min cost to get to it
            stair at n+1 compare its current min cost to this cost
            stair at n+1 just update it loolololoololloll
        '''
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2,n+1):
            dp[i] = min(cost[i-1] + dp[i-1],cost[i-2] + dp[i-2])
        
        return dp[n]
