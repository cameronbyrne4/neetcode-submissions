import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        Sort array in place in nlogn time
        Can't use sort
        should we heapify it?
        '''

        heapq.heapify(nums) # in place O(n)

        res = []
        while nums:
            cur = heapq.heappop(nums)
            res.append(cur)
        return res
