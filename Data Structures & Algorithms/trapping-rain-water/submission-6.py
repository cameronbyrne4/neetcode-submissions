class Solution:
    def trap(self, height: List[int]) -> int:
        """
        limited by whichever site is shorter no matter what

        Short side (tracking max) --> add to total --> move inward
        """
        total = 0
        n = len(height)
        l,r = 0, n-1
        maxleft, maxright = height[0], height[-1]

        while l<r:
            if maxleft < maxright: # move left one
                total += (maxleft-height[l])
                l += 1
                maxleft = max(maxleft, height[l])
            else:
                total += (maxright-height[r])
                r -= 1
                maxright = max(maxright, height[r])
        


        return total