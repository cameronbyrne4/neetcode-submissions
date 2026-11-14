class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        # how can we look at every subarray!
        # Maybe iterate thru i where i is the left?
        # but this is my O(n^2) solution that doesn't really do dp
        
        '''
        Solution
        - track max and min products as they come
        - 0 resets the current ones back to 1
        '''
        res = nums[0]
        curMax = 1
        curMin = 1
        for i in nums:
            #if i == 0:
                #curMax, curMin = 1, 1
            #else:
                temp = curMax
                curMax = max(curMax*i, curMin*i, i )
                curMin = min(curMin*i, temp*i, i )
                res = max(res, curMax)

        return res
        