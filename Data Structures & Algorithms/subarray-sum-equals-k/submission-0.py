from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        IDEA: have to permute all subarrays b/c you never know

        Solution: prefix sums then two sum method
        '''
        count = 0

        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        # Difference in prefix sums must be abs(k)

        setp = Counter()
        setp[0] = 1  # Start of array has 0 prefix
        
        for p in prefix:
            key = p-k  # but we have to only do earlier ones? yes so counter grows as we go
            if key in setp:
                count += setp[key]

            setp[p] += 1    #
        return count