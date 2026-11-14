class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            if n in d:
                return True
            d[n] += 1

        return False