class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        Shit solution is finding all double subarrays

        Branch solution:
            either put a number in array 1 or array 2
            compare the sums at the very end

        Thouhgts:
            finding 2 matching subset is the same thing as finding ANY subarray that
            sums up to half of the total

        Ok RETARD heres the deal
    
        '''
        total = sum(nums)

        # If we have an odd total we are done
        if total % 2 == 1:
            return False
        
        target = total / 2

        # For every element, we are adding it to our list of sums (dp).
        # check if the target is in that list OR if
        dp = set()
        dp.add(0)
        # going backwards thru numbs
        for i in range(len(nums)-1,-1,-1):
            nextround = dp.copy()
            val = nums[i]
            for k in dp:
                nextround.add(k + nums[i])
            dp = nextround.copy()
            if target in dp:
                return True
            
        return False