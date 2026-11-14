class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1   # Empty output  1 way to get to target of 0

        for i in range(target+1):
            for n in nums:
                # build up!
                if i + n <= target:
                    dp[i+n] += dp[i]

        
        return dp[target]