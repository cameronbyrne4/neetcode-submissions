class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        -- use pointers
        -- the worst version is brute force eww

        Strategy is to start on far sides and move the smaller pointer ONLY WHY??

        Formula for area with 2 fixed heights
         = ( j - i ) * min height
        '''

        res = 0
        l = 0
        r = len(heights)-1
        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            res = max(res, area)

            # Move the smaller
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1



        return res