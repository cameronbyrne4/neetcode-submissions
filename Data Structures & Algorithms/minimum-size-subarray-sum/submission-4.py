class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        No sorting cb window
        dynamic sliding window = 2 pointers
        luckily all are pos
        '''
        n = len(nums)
        min_len = float('inf')     # Updates when we find a subarray with the necessary sum
        cursum = nums[0]      # Updates with each pointer change
                        # Compare to target
        l,r = 0, 0
        

        while r < n:
            if cursum < target: # Too small --> move r, expand window
                r += 1
                if r < n:
                    cursum += nums[r]
            else:   # Big enough, now move l as much as we can
                while l <= r and cursum >= target:
                    min_len = min(min_len, r-l+1)
                    cursum -= nums[l]
                    l += 1


        if min_len == float('inf'):
            return 0
        else:
            return min_len