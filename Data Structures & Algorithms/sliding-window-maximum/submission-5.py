from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Deque monotonically decreasing**

        So, if a new value is increasing, we must pop from end until the deque is increasing once again

        Size is k
        """
        result = []
        q = deque()

        l = 0
        for r in range(len(nums)):
            # remove elements smaller than cur
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) # appendleft() is for front
            # remove elements no longer in window bounds
            while q[0] <= (r-k):
                q.popleft()

            # only need to add solution if we are in a valid window
            if r >= k-1:
                result.append(nums[q[0]])  # largest in q

        return result
