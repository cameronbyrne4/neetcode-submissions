class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        res = []
        subset = self.permute(nums[1:])

        for s in subset:
            for i in range(len(nums)):
                s_copy = s.copy()
                s_copy.insert(i, nums[0])
                res.append(s_copy)
        return res

