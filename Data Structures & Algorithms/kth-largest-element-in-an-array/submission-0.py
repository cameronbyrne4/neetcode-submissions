class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Rule: no sorting!
        # issue 1: duplicated

        # min heap, where we keep killing the top if we are over k!

        minheap = []
        for n in nums:
            heapq.heappush(minheap,n)
            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0] 