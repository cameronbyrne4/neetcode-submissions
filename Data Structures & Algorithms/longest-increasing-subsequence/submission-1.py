class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Okay so this is definitely weird.
        From every i:
            check how many times a counter val is increased before it hits the end
            compare this to the max
        This solution is O(n^2)

        See it depends on where we start:
        * if we have 4561234, its the 4 at the end

        Solution:
        for each i we look back to find the most recent number smaller than it
            increment that count by 1
            keep in dp
        
        return max in dp


        Actual solution:
        * work backwards
        * either keep as 1 or += 1 when
        '''
        # basically each dp is tracking the longest consecs after k, with k as the start
        dp = [1] * len(nums)
        for k in range(len(nums)-1, -1, -1):
            # Going reverse, pick the max + 1 of all the ones AFTER that are larger
            maxlen = 1
            for a in range(k+1, len(nums)):
                if nums[a] > nums[k]:
                    curlen = dp[a] + 1
                    maxlen = max(maxlen, curlen)
            dp[k] = maxlen

        return max(dp)