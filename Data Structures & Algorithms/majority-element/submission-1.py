class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        so simple
        make a hash
        if the count is under, ++
        if else, return the number
        '''
        h = Counter()
        limit = len(nums)/2

        for n in nums:
            h[n]+= 1
            if h[n] >= limit:
                return n
            
