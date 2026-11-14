class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Moving pointers inward

        If the H lower AND W lower, the area can't increase

        So ignore all cases when height doesn' grow

        Move left or right side??? the smaller one

        [1,15,100,2,2,3]
        '''
        l, r = 0, len(heights)-1
        maxarea = float("-inf")

        while l < r:
            print("lr:", l, r)
            maxarea = max(maxarea, ((r-l) * min(heights[l], heights[r])))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1


        return maxarea