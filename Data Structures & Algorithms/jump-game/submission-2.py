class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        -- use dp to attach a boolean to each jump height
        going backwards, if ANY of them in that range are true, then we are good
        '''
        goali = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goali:
                goali = i   # If we can reach the dynamic top from i, our new goal is to reach i


        if goali == 0:
            return True
        return False