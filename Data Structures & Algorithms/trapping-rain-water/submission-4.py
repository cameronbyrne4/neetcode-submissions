class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        1. amt of water at each index:
            top - bottom
            min(max left, max right) - height[i]

            but the min must be higher than the cur height


            2 passes to find the max height to left and right of each point
        '''
        n = len(height)
        prefixmax = [0] * n
        suffixmax = [0] * n

        # max to the left can ONLY increase
        curmax = 0
        for i in range(n):
            prefixmax[i] = curmax
            curmax = max(curmax, height[i])

        # max to the right?
        curmax = -1
        for i in range(n-1, -1, -1):
            suffixmax[i] = curmax
            curmax = max(curmax, height[i])

        total_rain = 0
        for i in range(n):
            top_height = min(suffixmax[i], prefixmax[i] )
            if top_height > height[i]:
                total_rain += top_height - height[i]
        return total_rain
