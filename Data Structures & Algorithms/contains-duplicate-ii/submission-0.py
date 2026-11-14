class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        dict
        {num : most recent index we saw it}

        encounter number:
            - check if in dict
            -   if yes, 

        '''

        d = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        
        return False