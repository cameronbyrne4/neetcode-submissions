class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Use 2 pointers
        Area based on height of smaller one
        can only increase if we move said smaller one inwards
        keep trying!
        '''
        res = float('-inf')
        n = len(heights)
        l,r = 0, n-1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            # move pointers greedily
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

        
