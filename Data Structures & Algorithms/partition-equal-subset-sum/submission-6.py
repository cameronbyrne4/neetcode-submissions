class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        t = sum(nums) // 2

        dp = [0] * (t + 1)
        dp[0] = 1

        for num in nums:
            for i in range(t, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return bool(dp[t])