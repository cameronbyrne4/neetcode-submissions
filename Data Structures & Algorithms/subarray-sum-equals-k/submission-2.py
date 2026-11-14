from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = 0
        p_freqs = defaultdict(int)
        p_freqs[0] = 1

        for i in range(len(nums)):
            # see if the diff is in prefix dict
            # add to prefix dict after
            prefix += nums[i]
            key = prefix - k # prefix - key = k
            if key in p_freqs:
                total += p_freqs[key]
            p_freqs[prefix] += 1

        return total