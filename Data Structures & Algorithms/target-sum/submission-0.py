class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        Seems like we can permute all the +/- possibilities

        Then tally how many of them equal the sum?

        sum(nums) is the largest we can go

        BACKTRACK OR DP

        1. backtrack = use base case( return 1 or 0) and recursion (return sum)
        '''
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]    # Represents how many each each sum can be formed using the first i numbers from i=0...n
        dp[0][0] = 1

        for i in range(n):
            for sums, count in dp[i].items():
                dp[i+1][sums + nums[i]] += count
                dp[i+1][sums - nums[i]] += count

        return dp[-1][target]       #{target: count}