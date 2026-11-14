from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        BUCKET SOrt:
        1. turn into conuter
        2. turn counter into an array of list, idx represents freq
        3. attack backwards

        TIPS:
        1. initializing arrays of stuff!
        '''

        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for key, val in counts.items():
            buckets[val].append(key)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            if buckets[i] == []:
                continue
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res



