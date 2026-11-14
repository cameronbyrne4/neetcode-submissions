class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        total = 0
        # populate each with max height preceeding it (including it)
        # monotonically increases
        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(height[i], prefix[i-1])

        suffix[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = max(height[i], suffix[i+1])

        # now sum up waters
        for i in range(n):
            # Vol = min height - bottom height
            vol = min(prefix[i], suffix[i]) - height[i]
            total += vol

        return total